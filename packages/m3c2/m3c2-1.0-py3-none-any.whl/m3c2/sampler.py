"""
samplermcmc.sampler
"""

import multiprocessing
import numpy as np
import os
import pickle
import sys
import time

from .chain import Chain
from .proposal import Prior, init_logger

TSTEP = np.array([25.2741, 7., 4.47502, 3.5236, 3.0232,
                  2.71225, 2.49879, 2.34226, 2.22198, 2.12628,
                  2.04807, 1.98276, 1.92728, 1.87946, 1.83774,
                  1.80096, 1.76826, 1.73895, 1.7125, 1.68849,
                  1.66657, 1.64647, 1.62795, 1.61083, 1.59494,
                  1.58014, 1.56632, 1.55338, 1.54123, 1.5298,
                  1.51901, 1.50881, 1.49916, 1.49, 1.4813,
                  1.47302, 1.46512, 1.45759, 1.45039, 1.4435,
                  1.4369, 1.43056, 1.42448, 1.41864, 1.41302,
                  1.40761, 1.40239, 1.39736, 1.3925, 1.38781,
                  1.38327, 1.37888, 1.37463, 1.37051, 1.36652,
                  1.36265, 1.35889, 1.35524, 1.3517, 1.34825,
                  1.3449, 1.34164, 1.33847, 1.33538, 1.33236,
                  1.32943, 1.32656, 1.32377, 1.32104, 1.31838,
                  1.31578, 1.31325, 1.31076, 1.30834, 1.30596,
                  1.30364, 1.30137, 1.29915, 1.29697, 1.29484,
                  1.29275, 1.29071, 1.2887, 1.28673, 1.2848,
                  1.28291, 1.28106, 1.27923, 1.27745, 1.27569,
                  1.27397, 1.27227, 1.27061, 1.26898, 1.26737,
                  1.26579, 1.26424, 1.26271, 1.26121,
                  1.25973])


def set_temperature(dim, nTemp, Tmax=None):
    """ Set initial temperature ladder. 
    """
    if Tmax is None:
        if dim > TSTEP.shape[0]:
            # An approximation to the temperature step at large dimension
            tstep = 1.0 + 2.0*np.sqrt(np.log(4.0))/np.sqrt(dim)
        else:
            tstep = TSTEP[int(dim)-1]
        Tmax = tstep**(nTemp -1)
    else:
        tstep = np.exp(np.log(Tmax)/(nTemp-1))
    betas = np.logspace(0, -np.log10(Tmax), nTemp)
    return Tmax, betas

class Sampler:
    """ A multi chains MCMC
    """

    def __init__(self, Nchains, priors, loglik, logpi, param_dic,
                 cov=True, nmodes=False, kde=False, 
                 logger=None, profiling=False, debug=False):
        """ Configuration of a MCMC sampler. 
        """
        self.priors = priors
        self.Nchains = Nchains
        self.log_l = loglik  
        self.log_p = logpi
        self.dim = len(param_dic)
        self.par_dict = param_dic
        self.logger = init_logger() if logger is None else logger
        self.chains = [Chain(1, 0, loglik, logpi, logger=self.logger, profiling=profiling, debug=debug)
                       for c in range(Nchains)]
        self.debug = debug
        self.profiling = profiling
        self.compute_cov = cov
        self.compute_nmodes = nmodes
        self.compute_kde = kde
        
    def set_starting_point(self, pars_sampl):
        """Initialize chain data with a first sample.
        """
        assert len(pars_sampl) == self.Nchains
        for ic, p in enumerate(pars_sampl):
            lik = self.log_l(p)
            prior = self.log_p(p)
            self.chains[ic].add(p, lik, prior, is_max=True)
            if self.compute_cov:
                self.chains[ic].init_cov()  

    def set_proposals(self, p=None):
        """Set list of proposals for each chain. 
        
        p takes the form of a dictionary (or list of dictionaries, one
        for each chain), with keys corresponding to proposal function
        and values to probabilty of using it.  
        """
        if p is None:
            P = Prior(self.par_dict, self.priors)
            p = {P.sample_prior:100}
        if isinstance(p, dict):
            p = [p]*self.Nchains
        for cp, chain in zip(p, self.chains):
            chain.set_proposals(cp)
            names = [k.__self__.name for k,v in cp.items()]
            if 'SCAM' in names and not self.compute_cov:
                self.logger.error("'cov' option needed to use SCAM proposal")
            if 'ReMHA' in names and not self.compute_nmodes:
                self.logger.error("'nmodes' option needed to use ReMHA proposal")
            if 'adaptKDE' in names and not self.compute_kde:
                self.logger.error("'kde' option needed to use adaptKDE proposal")

    def resume(self, filenames, thin=1, adapt=1000):
        """Resume chains from previous run.

        Data files contains series of point and their associated
        likelihood as an (npt x npars+1) array
        """
        assert len(filenames)==self.Nchains
        self.outdir = os.path.dirname(filenames[0])

        dat = [np.load(filenames[ni])[::thin] for ni in range(self.Nchains)]
        logL_in_file = False if self.dim==dat[0].shape[1] else True
        for ni, d in enumerate(dat):
            for ims in range(len(d)):
                pt = d[ims,:-1] if logL_in_file else d[ims,:]
                lik = d[ims,-1] if logL_in_file else self.log_l(pt)
                prior = self.log_p(pt)

                is_max = lik > self.chains[ni].maxL 
                self.chains[ni].add(pt, lik, prior, is_max=is_max)

            self._adapt_chain(ni, ims)

                
    def save_to_disk(self, num=None, stats=False, debug=False):
        """Save chain data (points and associated likelihood) to numpy file.

        Data files contains series of point and their associated
        likelihood as an (npt x npars+1) array
        """
        lnum = range(self.Nchains) if num is None else [num]
        for num in lnum:
            fn = os.path.join(self.outdir, f"chain_{num}.npy")
            T = np.append(np.array(self.chains[num].chn),
                          np.array(self.chains[num].logL, ndmin=2).T, axis=1)
            np.save(fn, T, allow_pickle=False)
        if stats and self.profiling:
            for num in lnum:
                fn = os.path.join(self.outdir, f"stats_{num}.pkl")
                S = dict()
                for k in self.chains[num].jumps.keys():
                    S[k] = dict({"njump":self.chains[num].jumps[k], "ar":self.chains[num].ar[k]})
                S["nswap_accepted"] = self.chains[num].swap_accepted
                S["nswap_proposed"] = self.chains[num].swap_proposed
                pickle.dump(S, open(fn, 'wb'))
        if debug:
            for num in lnum:
                fn = os.path.join(self.outdir, f"all_data_{num}.pkl")
                S = self.chains[num].history()
                pickle.dump(S, open(fn, 'wb'))

    def run_mcmc(self, niter, adapt=1000, printN=2000, outdir='./', multiproc=True, seeds=None):
        """Run MCMC using multiprocessing. 
    
        Args:
        niter: number of mcmc iteration
        adapt: number of iteration before updating covariance, modes
        printN: number of iteration before printing convergence info
        outdir: directory where to save chain data
        multiproc: enabling/disabling multiprocessing 
        
        Returns:
        list of Chain objects: see output files to get accumulated points and statistics.

        """
        self.adapt = adapt
        self.printN = printN
        self.outdir = outdir
        if not multiproc:
            return self._run_mcmc_sequential(niter)
        if seeds is None:
            seeds = [None]*self.Nchains
        
        lock = multiprocessing.Lock()
        process = [multiprocessing.Process(target=self._run_proc, args=(num, niter, lock, seeds[num]))
                   for num in range(self.Nchains)]
        for p in process:
            p.start()
        for p in process:
            p.join()
        self.logger.debug("End of the MCMC run. Closing the pipes and processes.")

        while process:
            proc = process.pop()
            self.logger.debug("closing process")
            if proc.is_alive():
                proc.terminate()
                self.logger.debug("term signal sent")
        self.logger.info("Done !")
        return self.chains

    def _adapt_chain(self, ni, ims):
        """ Update chains covariance, nmodes and kde.  
        """
        if self.compute_cov:
            self.chains[ni].update_cov()
        if self.compute_nmodes:
            if (1.0/self.chains[ni].beta <= 10.0) and ims >= 10*self.adapt:
                self.chains[ni].update_modes()
        if self.compute_kde and ims>0 and ims%5000 == 0 and\
           self.chains[ni].kde_tracker.upkde: 
            self.chains[ni].update_kde()
            if self.profiling:
                fn = os.path.join(self.outdir, f"kde_{ni}_{ims}.pkl")
                pickle.dump(self.chains[ni].kde, open(fn, 'wb'))

    
    def _run_mcmc_sequential(self, niter):
        """ Run chains sequentially. 
        """
        for ims in range(niter):
            
            if ims%self.printN == 0:
                self.logger.info(f"iter {ims}")
                for num in range(self.Nchains):
                    self.logger.info(f"chain {num}")
                    self.chains[num].print_info()
                if ims>0:
                    self.save_to_disk(stats=True)
                    
            if ims%self.adapt == 0 and ims!= 0: # update cov and modes
                for num in range(self.Nchains):
                    self._adapt_chain(num, ims)

            for num in range(self.Nchains):
                self.chains[num].full_step(ims, chains=self.chains)

        self.save_to_disk(stats=True)
        return self.chains

    def _run_proc(self, num, niter, lock, seed):
        """Run a chain #num in a dedicated process.
        """
        if seed is None:
            np.random.seed((os.getpid() * int(time.time())) % 123456789)
        else:
            np.random.seed(seed)
            
        for ims in range(niter):

            if ims%self.printN == 0 or ims==niter-1: # print and save to disk
                lock.acquire()
                self.logger.info(f"iter {ims} chain {num}")
                self.chains[num].print_info()
                lock.release()
                self.save_to_disk(num=num, stats=True)

            if ims%self.adapt == 0 and ims!= 0: # update cov and modes
                self._adapt_chain(num, ims)

            y, Ly, Py = self.chains[num].full_step(ims, chains=self.chains) # go one step

        self.save_to_disk(num=num, stats=True)

                
class PTSampler(Sampler):
    """ A parallel tempering MCMC. 
    """

    def __init__(self, Nchains, priors, loglik, logpi, param_dic, Tmax=None,
                 cov=True, nmodes=False, kde=False, 
                 logger=None, profiling=False, debug=False):
        """ Configuration of a ptMCMC sampler. 
        """
        super().__init__(Nchains, priors, loglik, logpi, param_dic, logger=logger, profiling=profiling, cov=cov, nmodes=nmodes, kde=kde)
        Tmax, betas = set_temperature(self.dim, self.Nchains, Tmax=Tmax)
        self.Tmax = Tmax
        self.logger.info(f'Tmax={Tmax}, range of temperature: {1/betas}')
        self.dS = np.log(np.diff(1/betas))
        dbeta = [betas[j]-betas[j+1] for j in range(self.Nchains-1)]+[0]
        self.chains = [Chain(betas[c], dbeta[c], loglik, logpi, logger=self.logger, profiling=profiling,
                             debug=debug)
                       for c in range(Nchains)]
        self.debug = debug

    def swap_elligibility(self, num, ims, Ly0, Ly1):
        """Check if two chains can swap given their current log-lik Ly0 and
        Ly1.
        """
        if ims<self.ims0:
            return False
        if np.random.random() > self.pSwap:
            return False
        self.chains[num].swap_proposed += 1
        dbeta = self.chains[num].dbeta1
        alpha = np.log(np.random.random())
        dlogl = dbeta*(Ly1 - Ly0)
        res = dlogl >= alpha
        return res 

    def swap(self, num, ims, y0, Ly0, y1, Ly1):
        """Perform chain swap. 
        """
        self.chains[num].Mx = y1
        self.chains[num+1].Mx = y0
        self.chains[num+1].Lx = Ly0
        self.chains[num].Lx = Ly1
        Px1 = self.chains[num+1].Px
        self.chains[num+1].Px = self.chains[num].Px
        self.chains[num].Px = Px1
        self.chains[num].swapped()
        if self.debug:
            self.chains[num].full_win.append(Ly1)
            self.chains[num].full_swap.append(ims)
            
            
    def adjust_temp(self, ims, ratio, betas):
        """Adjust temperature ladder. 
        """
        ratio = ratio[:-1] # n-1 swap for n chains
        decay = self.adapt_t0 / (ims + self.adapt_t0)
        kappa = decay / self.adapt_nu
        dS = kappa * (ratio[:1] - ratio[1:])
        deltaTs = np.diff(1/betas[:-1])
        deltaTs *= np.exp(dS)
        new_beta = betas.copy()
        new_beta[1:-1] = 1/(np.cumsum(deltaTs)+1)
        new_beta[new_beta<1/self.Tmax] = 1/self.Tmax
        dbeta = [new_beta[j] - new_beta[j+1] for j in range(self.Nchains-1)]
        dbeta.append(0)
        beta = new_beta 
        return beta, dbeta
            
    def _init_pipe(self):
        """ Initialize communication pipes between pairs of chains. 

        Used to exchange points
        """
        conns = [multiprocessing.Pipe() for num in range(self.Nchains)]
        self.child_conn = [conns[num][1] for num in range(self.Nchains)]
        self.parent_conn = [conns[num+1][0] for num in range(self.Nchains-1)]
        self.parent_conn.append(None)

        conns = [multiprocessing.Pipe() for num in range(self.Nchains)]
        self.swap_child_conn = [conns[num+1][1] for num in range(self.Nchains-1)]
        self.swap_parent_conn = [conns[num][0] for num in range(self.Nchains)]
        self.swap_child_conn.append(None)

        
    def _init_bcast_pipe(self):
        """ Initialize communication pipes between all chains. 
        
        Used to exchange beta
        """
        conns = [multiprocessing.Pipe() for num in range(self.Nchains)]
        self.bcast_parent1_conn = [conns[num][0] for num in range(self.Nchains)]
        self.bcast_child1_conn = [conns[num][1] for num in range(self.Nchains)]
        conns = [multiprocessing.Pipe() for num in range(self.Nchains)]
        self.bcast_parent2_conn = [conns[num][0] for num in range(self.Nchains)]
        self.bcast_child2_conn = [conns[num][1] for num in range(self.Nchains)]
        
    # def _init_chains(self):
    #     """ Initialize a shared data container
    #     """
    #     manager = multiprocessing.Manager()
    #     chains = manager.list()
    #     for chain in self.chains:
    #         chain.share_data(manager)

    def run_mcmc(self, niter, pSwap=0.5, adapt=1000, adapt_tN=10, n0_swap=2500, printN=2000,
                 adapt_t0=1000., adapt_nu=100., outdir='./', multiproc=True, seeds=None):
        """Run ptMCMC using multiprocessing. 
    
        Args:
        niter: number of mcmc iteration
        pSwap: probability of swapping chains
        n0_swap: number of iteration before starting swap
        adapt: number of iteration before updating covariance, modes
        adapt_tN: number of iteration before adjusting temperature ladder
        adapt_t0: temperature adaptation lag
        adapt_nu: temperature adaptation time
        printN: number of iteration before printing convergence info
        outdir: directory where to save chain data
        multiproc: enabling/disabling multiprocessing 
        
        Returns:
        list of Chain objects: see output files to get accumulated points and statistics.

        """
        self.ims0 = n0_swap
        self.pSwap = pSwap
        self.adapt = adapt
        self.adapt_t = adapt_tN
        self.adapt_t0 = adapt_t0
        self.adapt_nu = adapt_nu
        self.printN = printN
        self.outdir = outdir
        if not multiproc:
            return self._run_mcmc_sequential(niter)

        if seeds is None:
            seeds = [None]*self.Nchains
        lock = multiprocessing.Lock()
        self._init_pipe() ; conns = [self.child_conn, self.parent_conn]
        #self._init_chains()
        if niter>self.adapt_t:
            self._init_bcast_pipe()
            conns += [self.bcast_child2_conn, self.bcast_child1_conn,
                      self.bcast_parent2_conn, self.bcast_parent1_conn]
        process = [multiprocessing.Process(target=self._run_proc, args=(num, niter,
                                                                        self.child_conn[num],
                                                                        self.parent_conn[num],
                                                                        lock, seeds[num]))
                   for num in range(self.Nchains)]

        if niter>self.adapt_t:
            process.append(multiprocessing.Process(target=self._adjust_temp_proc, args=(niter,lock)))

        for p in process:
            p.start()
        for p in process:
            p.join()

        self.logger.debug("End of the MCMC run. Closing the pipes and processes.")

        for conn in conns:
            for j,c in enumerate(self.chains):
                self.logger.debug(f"Closing pipe {j}")
                if conn[j] is not None:
                    conn[j].close()
            
        while process:
            proc = process.pop()
            self.logger.debug("closing process")
            if proc.is_alive():
                proc.terminate()
                self.logger.debug("term signal sent")
        
        self.logger.info("Done !")
        return self.chains
        
    def _run_mcmc_sequential(self, niter):
        """ Run chains sequentially. 
        """
        #Nswap = 1
        for ims in range(niter):
            
            if ims%self.printN == 0:
                self.logger.info(f"iter {ims}")
                for num in range(self.Nchains):
                    self.logger.info(f"chain {num}")
                    self.chains[num].print_info()
                if ims>0:
                    self.save_to_disk(stats=True, debug=self.debug)
                    
            if ims%self.adapt == 0 and ims!= 0: # update cov and modes
                for num in range(self.Nchains):
                    self._adapt_chain(num, ims)

            for num in range(self.Nchains):
                self.chains[num].full_step(ims, chains=self.chains)

                #for num in range(self.Nchains-2,-1,-1):#self.Nchains-1):
                if num!= self.Nchains-1:
                    y1, Ly1 = self.chains[num+1].Mx, self.chains[num+1].Lx
                    y, Ly = self.chains[num].Mx, self.chains[num].Lx

                    if self.swap_elligibility(num, ims, Ly, Ly1):
                        self.swap(num, ims, y, Ly, y1, Ly1)

                if self.debug:
                    self.chains[num].full_temp.append(1/self.chains[num].beta)
                    self.chains[num].full_acc.append(self.chains[num].swap_accepted)
                    self.chains[num].full_prop.append(self.chains[num].swap_proposed)

            if ims>=self.ims0 and ims%self.adapt_t == 0 and ims!= 0: # update temperature ladder
                ratio = np.array([c.get_ratio() for c in self.chains])
                betas = np.array([c.beta for c in self.chains])
                beta, dbeta = self.adjust_temp(ims, ratio, betas)
                for j,c in enumerate(self.chains):
                    c.beta = beta[j]
                    c.dbeta1 = dbeta[j]

        self.save_to_disk(stats=True, debug=self.debug)
        return self.chains
    
    def _adjust_temp_proc(self, niter, lock):
        """Run temperature ladder adjustement in a dedicated process. 
        """
        for ims in range(niter):
            if ims>=self.ims0 and ims%self.adapt_t == 0 and ims!= 0: 
                res = [self.bcast_parent1_conn[num].recv() for num in range(self.Nchains)]
                betas = np.array([r[2] for r in res])
                nswap_a = np.array([r[0] for r in res])
                nswap_p = np.array([r[1] for r in res])
                ratio = nswap_a / nswap_p
                beta, dbeta = self.adjust_temp(ims, ratio, betas)
                lock.acquire()
                for j,c in enumerate(self.chains):
                    self.bcast_child2_conn[j].send([beta[j], dbeta[j]])
                    #c.beta = beta[j]
                    #c.dbeta1 = dbeta[j]
                lock.release()
        lock.acquire()
        self.logger.info("Temperature ladder adjustment processus is done")
        lock.release()
        
    def _run_proc(self, num, niter, conn, other_conn, lock, seed):
        """Run a chain #num in a dedicated process.
        
        Communications are managed through multiprocessing pipes and
        data are shared using multiprocessing managers.

        """
        if seed is None:
            np.random.seed((os.getpid() * int(time.time())) % 123456789)
        else:
            np.random.seed(seed)
        Ly2 = 0.
        
        for ims in range(niter):

            if self.debug and ims%100 == 0:
                self.chains[num].time_iter.append(time.time())
            
            if ims%self.printN == 0 or ims==niter-1: # print and save to disk
                lock.acquire()
                self.logger.info(f"iter {ims} chain {num}")
                self.chains[num].print_info()
                lock.release()
                self.save_to_disk(num=num, stats=True, debug=self.debug)

            if ims%self.adapt == 0 and ims!= 0: # update cov and modes
                self._adapt_chain(num, ims)

            y, Ly, Py = self.chains[num].full_step(ims, chains=self.chains) # go one step

            # swap
            if ims>=self.ims0:
                has_swapped = False
                if num>0:
                    conn.send([y, Ly, Py]) # data exchange for swap
                if other_conn is not None:
                    y1, Ly1, Py1 = other_conn.recv()
                    tosend = [y1, Ly1, Py1]
                    if self.swap_elligibility(num, ims, Ly, Ly1) and Ly!=Ly1:
                        self.chains[num].set_current(y1, Ly1, Py1)
                        self.chains[num].swapped()
                        has_swapped = True
                        tosend = [y, Ly, Py]
                        if self.debug:
                            self.chains[num].full_win.append(Ly1)
                            self.chains[num].full_swap.append(ims)
                if num>0:
                    yN, LyN, PyN = self.swap_parent_conn[num].recv()
                    if LyN!=Ly and other_conn is not None: #choose between n+1/n-1 swap
                        if has_swapped:
                            tosend = [yN, LyN, PyN] # forward
                        else:
                            tosend = [y1, Ly1, Py1] # update
                            self.chains[num].set_current(yN, LyN, PyN)
                if other_conn is not None:   
                    self.swap_child_conn[num].send(tosend)

            # debug
            if self.debug:
                self.chains[num].full_temp.append(1/self.chains[num].beta)
                self.chains[num].full_acc.append(self.chains[num].swap_accepted)
                self.chains[num].full_prop.append(self.chains[num].swap_proposed)

            # adjust temperature ladder
            if ims>=self.ims0 and ims%self.adapt_t == 0 and ims!= 0: 
                self.bcast_child1_conn[num].send([self.chains[num].swap_accepted,
                                                  self.chains[num].swap_proposed,
                                                  self.chains[num].beta])
                beta, dbeta1 = self.bcast_parent2_conn[num].recv()
                self.chains[num].beta = beta
                self.chains[num].dbeta = dbeta1

        self.save_to_disk(num=num, stats=True, debug=self.debug)

