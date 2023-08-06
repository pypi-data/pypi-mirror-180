"""
samplermcmc.chain
"""
import copy
import acor._acor as acor
import numpy as np
import multiprocessing.managers
from sklearn.mixture import BayesianGaussianMixture as BGM
import sys
import multiprocessing
import time
try:
    from hyperkde import HyperKDE
except ImportError:
    pass
    
ACOR_MAXLAG = 10

def get_autocorr_len(chn, burn=0.25):
    """ Slim chain to retain un-correlated samples. 
    """
    xs = np.copy(np.array(chn))
    SzChn = int((1-burn) * np.shape(xs)[0]) ### skip first 25% of the chain
    xs = xs[SzChn:, :]
    
    try:
        al, mean, std = acor.acor(xs[:, 0], ACOR_MAXLAG)
    except:
        return 1
    for jj in range(1, np.shape(xs)[1]):
        xtmp = xs[:, jj]
        ac = 10000
        try:
            ac = acor.acor(xs[:, jj], ACOR_MAXLAG)[0]
        except:
            pass
        if ac < al:
            al = ac
    if al > 100:
        al = np.random.uniform(10., 100.)
    if al < 1.0 or np.isnan(al):
        al = 1
    return int(al)

class ChainData:
    """A container for chain shared data. 

    """
    def __init__(self, beta=1):
        """ Define data containers as attributes
        """
        self.beta = beta
        
    def to_dict(self):
        """ Return a dict to be shared accros process. 
        """
        d = dict()
        for k,v in vars(self).items():
            d[k] = v
        return d

class KDETracker:
    """ Monitor KDE evolution to identify a stable and good model. 
    """

    def __init__(self, logger):
        """ Create containers
        """
        self.kl = [] # used by kde
        self.dKL = 1.
        self.upkde = True
        self.count_groups = True
        self.count_dict = {}
        self.kde_groups_idx = None
        self.kde_paramlists = None
        self.logger = logger
        
    def counting(self, kde, ncount):
        """ Count group occurence. 
        """
        key = '_'.join(['.'.join(pl) for pl in kde.paramlists]) 
        if key in [*self.count_dict]: 
            self.count_dict[key] += 1 
            if self.count_dict[key] == ncount:
                self.count_groups = False
                self.kde_groups_idx = kde.groups_idx
                self.kde_paramlists = kde.paramlists
        else: 
            self.count_dict[key] = 1

    def set_kl(self, kde1, kde0):
        """ Compute Kullback Leiber divergence between 2 KDE. 
        """
        if self.count_groups:
            self.counting(kde1, 5)
            kl = None
        else:
            kl = kde0.get_KL(kde1) if kde0 is not None else None

        if kl is not None:
            self.kl.append(kl)
            self.logger.info(f"Adding KL={kl}")
        return kl

    def check_stability(self):
        """ Check if KDE model is stable by looking at kl evolution. 
        """
        if len(self.kl)<=5:
            return
        akl = np.array(self.kl)
        dKL = abs(np.mean(np.diff(akl[-5:])))
        mean_kl = np.sqrt(np.mean(akl[-5:]**2))
        self.dKL = dKL / mean_kl
        self.logger.info(f"Updating dKL to {self.dKL}")
        self.upkde = self.dKL > 0.05 
    
class Chain:
    """ A tempered chain and its associated proposals.  
    """
    def __init__(self, beta, dbeta, log_l, log_p, logger=None, profiling=False, debug=False):
        """ Initialize a chain data container. 
        """
        #self.data = ChainData(beta).to_dict()
        self.maxL = -np.inf
        self.maxP = -np.inf
        self.chn = []
        self.logL = []
        self.logP = []
        self.modes = []
        self.cov = 0
        self.U = 0
        self.S = 0
        self.kde = None
        self.Px = 0
        self.Lx = 0
        self.beta = beta
        self.dbeta1 = dbeta
        self.swap_accepted = 1
        self.swap_proposed = 1

        
        self.props = {}
        self.anneal = 1
        self.log_l = log_l
        self.log_p = log_p
        self.logger = logger
        self.profiling = profiling
        if profiling:
            self.jumps = {}
            self.ar = {}
        self.debug = debug
        if debug:
            self.full_chn = [] 
            self.full_win = []
            self.full_swap = []
            self.full_temp = [] 
            self.full_acc = [] 
            self.full_prop = [] 
            self.full_proposal = []
            self.time_cov = []
            self.time_nmodes = []
            self.time_proposal = {}
            self.time_iter = []
        self.shared = False
        self.kde_tracker = KDETracker(self.logger)
        
    def history(self):
        S = dict()
        if self.debug:
            S['full_chn'] = self.full_chn
            S['full_win'] = self.full_win
            S['full_temp'] = self.full_temp
            S['full_swap'] = self.full_swap
            S['full_acc'] = self.full_acc
            S['full_prop'] = self.full_prop
            S['full_proposal'] = self.full_proposal
            S['time_proposal'] = self.time_proposal
            S['time_cov'] = self.time_cov
            S['time_nmodes'] = self.time_nmodes
            S['time_iter'] = self.time_iter
            for k,v in self.props.items():
                S.update(k.__self__.history())
        return S
            
    def init_cov(self, cov=None):
        """Initialize the covariance matrix and its SVD decomposition.
        """
        if cov is None:
            cov = np.diag(np.ones(len(self.Mx))*0.01**2)
        self.cov = cov
        self.U, self.S, v = np.linalg.svd(cov)
        
    # def share_data(self, manager):
    #     """Convert data container into a shared container, using
    #     multiprocessing.manager.

    #     """
    #     d = manager.dict()
    #     for k,v in self.data.items():
    #         d[k] = v
    #     self.data = d
    #     self.shared = True

    def set_current(self, y, Ly, Py):
        """ Set the current point
        """
        self.Mx = y
        self.Lx = Ly
        self.Px = Py
        
    def add_current(self):
        """ Add current point Mx to the list of accumulated points. 
        """
        self.chn.append(self.Mx)
        self.logL.append(self.Lx)
        self.logP.append(self.Px)
        
    def add(self, p, lik, prior, is_max=False):
        """ Add a new point and update Mx, logL, logP, Lx, Px
        
        if is_max is True, also update maxL and maxP. 
        """
        self.chn.append(p)
        self.Mx = p
        self.logL.append(lik)
        self.Lx = lik
        self.logP.append(lik+prior)
        self.Px = lik+prior
        if is_max:
            self.maxP = self.Px
            self.maxL = self.Lx
                
    # @property
    # def Mx(self):
    #     """ Current model point.
    #     """
    #     return self.data['Mx']
    # @Mx.setter
    # def Mx(self, value):
    #    self.data['Mx'] = value 

    def set_proposals(self, props):
        """ Set list of proposal with their associated weights. 
        """
        wtot = np.array(list(props.values())).sum()
        for k,v in props.items():
            props[k] = float(v)/wtot
        self.props = props
        if self.profiling:
            for k,v in self.props.items():
                kk = k.__self__.name
                self.jumps[kk] = 0
                self.ar[kk] = 0
                if self.debug:
                    self.time_proposal[kk] = []
       
    def choose_proposal(self):
        """ Randomly choose a proposal, along given weights. 
        """
        kys = list(self.props.keys())
        i_p = np.random.choice(len(kys), p=np.array(list(self.props.values())))
        p = list(self.props.keys())[i_p]
        if self.profiling:
            self.jumps[p.__self__.name] += 1
        return p
    
    def get_size(self):
        """ Return size of the chain. 
        """
        return len(self.chn)

    def get_sample(self, i):
        """ Return sample for a given indice. 
        """
        return self.chn[i]

    def get_ratio(self):
        """ Return acceptance ratio
        """
        return self.swap_accepted/self.swap_proposed
    
    def swapped(self):
        """ Gather chain swap statistics. 
        """
        self.swap_accepted += 1

    def _full_step_debug(self, ims, chains=None):
        """
        """
        prop = self.choose_proposal()
        kprop = prop.__self__.name
        t0 = time.time()
        y, status, Ly, qxy = prop(self.Mx, chain=self, chains=chains, ims=ims)
        if Ly is None:
            Ly = self.log_l(y, i=ims, T=1/self.beta)
        self.time_proposal[kprop].append(time.time()-t0)

        # accept or reject
        if status==1:# accept in any case (slice like)
            self.add(y, Ly, self.log_p(y), is_max=(Ly > self.maxL))
            self.ar[kprop] += 1
            self.full_chn.append(Ly)
            self.full_proposal.append(kprop)
        elif status==0:
            accepted = self.MH_step(y, Ly, qxy) #accept or not
            if accepted:
                self.ar[kprop] += 1
                self.full_chn.append(Ly)
                self.full_proposal.append(kprop)
            else:
                self.full_chn.append(np.nan)
                self.full_proposal.append(kprop)
        elif status==-1 and self.profiling:# not really considered (like below threshold)
            self.jumps[kprop] -= 1
            self.full_chn.append(np.nan)
            self.full_proposal.append(kprop)
        return self.Mx, self.Lx, self.Px

        
    def full_step(self, ims, chains=None):
        """ Update current point using a proposal. 
        """
        # new point
        if self.debug:
            return self._full_step_debug(ims, chains=chains)
        prop = self.choose_proposal()
        kprop = prop.__self__.name
        y, status, Ly, qxy = prop(self.Mx, chain=self, chains=chains, ims=ims)
        if Ly is None:
            Ly = self.log_l(y, i=ims, T=1/self.beta)

        # accept or reject
        if status==1:# accept in any case (slice like)
            self.add(y, Ly, self.log_p(y), is_max=(Ly > self.maxL))
            if self.profiling:
                self.ar[kprop] += 1
        elif status==0:
            accepted = self.MH_step(y, Ly, qxy) #accept or not
            if self.profiling and accepted:
                self.ar[kprop] += 1
        elif status==-1 and self.profiling:# not really considered (like below threshold)
            self.jumps[kprop] -= 1
        return self.Mx, self.Lx, self.Px
        
    def MH_step(self, y, Ly, qxy):
        """ Performs Metropolis-Hastings selection
        """
        if not np.isfinite(Ly):
            self.add_current()
            return
        x = self.Mx
        pi_y  = self.log_p(y)
        log_MH =  (Ly - self.Lx)*self.beta + qxy + pi_y - self.log_p(x)
        log_alp = np.log(np.random.random())
        if log_MH > log_alp:
            is_max = Ly > self.maxL
            self.add(y, Ly, pi_y, is_max=is_max)
            return True
        else:
            self.add_current()
            return False

    def update_cov(self):
        """ Update covariance matrix and its SVD decomposition. 
        """
        t0 = time.time()
        al = get_autocorr_len(self.chn, burn=0.25)
        istart = int(0.75 * len(self.chn)) # skip first 25% of the chain
        x_tot = np.array(self.chn)[istart:-1:int(al)]
        cov = np.cov(x_tot.T)
        self.cov = cov
        self.U, self.S, v = np.linalg.svd(cov)
        if self.debug:
            self.time_cov.append(time.time()-t0)

    def update_kde(self, burn_frac=0.25, n_samples=5000):
        """ Update hyperKDE. 
        """
        #al = get_autocorr_len(self.chn, burn=burn_frac)
        burn = int(burn_frac*len(self.chn))
        chains = np.copy(np.array(self.chn))[burn:]
        down = max(len(chains)//n_samples, 1)
        chains = chains[0:-1:down]
        chains = chains[-n_samples:,:]
        self.logger.info(f"Build KDE with {len(chains)} samples, downsampling of {down}")
        
        names = np.array([f"p{i}" for i in range(len(self.Mx))])
        try:
            kde = HyperKDE(list(names), chains, names, 0.2, n_kde_max=1,
                           use_kmeans=False, global_bw=True,
                           groups_idx=self.kde_tracker.kde_groups_idx,
                           paramlists=self.kde_tracker.kde_paramlists)
            new, q = kde.draw_from_random_hyp_kde(chains[:,-1])
            assert np.isnan(new).sum()==0
        except:
            self.logger.info(f"Can't build KDE on {len(chains)} samples")
            return

        kl = self.kde_tracker.set_kl(kde, self.kde)
        self.kde_tracker.check_stability()
        self.kde = kde
        return kl

    def update_modes(self, tol=0.000001, reg_covar=1e-16):
        """ Update modes using BayesianGaussian Mixture. 

        ### FIXME: TODO: tolerance and
        ### regularization are hardcoded instead I need to do
        ### re-parametrization to make sure we do not need 1e-16
        ### FIXME: Restrict number of modes to 10
        """
        t0 = time.time()
        xs = np.copy(self.chn)
        SzChn = int(0.75 * np.shape(xs)[0]) ### skip first 25% of the chain
        xs = xs[SzChn::10, :] ### and we take every 10th
        
        ### I use BayesianGaussian Mixture and low bound on likelihood
        ### to identify the modes
        n_comp = 1
        gmm = BGM(n_components=n_comp,  tol=tol, reg_covar=reg_covar, covariance_type='full').fit(xs)
        ll_c = gmm.lower_bound_
        modes = []
        for ic in range(n_comp):
            modes.append([gmm.means_[ic, :], gmm.covariances_[ic, :,:], gmm.weights_[ic]])

        for n_comp in range(2,11):
            gmm = BGM(n_components=n_comp,  tol=tol, reg_covar=reg_covar, covariance_type='full').fit(xs)
            llmax = gmm.lower_bound_
            gm_max = copy.deepcopy(gmm)
            for ntr in range(5):
                gmm = BGM(n_components=n_comp,  tol=tol, reg_covar=reg_covar, covariance_type='full').fit(xs)
                if (gmm.converged_):
                    ll = gmm.lower_bound_
                    if ll > llmax:
                        llmax = ll
                        gm_max = copy.deepcopy(gmm)
            if (llmax - ll_c)/llmax > 0.02:
                modes = []
                for ic in range(n_comp):
                    modes.append([gm_max.means_[ic, :], gm_max.covariances_[ic, :,:], gm_max.weights_[ic]])
                ll_c = llmax
            else:
                break
        self.modes = modes
        if self.debug:
            self.time_nmodes.append(time.time()-t0)

    def print_info(self):
        """ Print log-likelihood info. 
        """
        self.logger.info(f"current loglik: {self.Lx:.1f}, "\
                         f"best: {self.maxL:.1f}, "\
                         f"temp: {1./self.beta:.1f}, "\
                         f"ratio: {self.get_ratio()}")
