"""
samplermcmc.proposal
"""

import numpy as np
import sys
try:
    from hyperkde import HyperKDE
except ImportError:
    HyperKDE = None

def init_logger():
    """ Default logger is stdout. 
    """
    from importlib import reload  # Not needed in Python 2
    import logging
    reload(logging)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    return logging.getLogger()
    
class Proposal:
    """A proposal function. We use a class to stored meta-data and ease
    the customization.
    """

    def __init__(self, names, logger=None, sort_name=None, sort_range=None):
        """Default initialization. 

        Number of parameters and their names are set here.
        sort_range: (1st index use to reshape, first axis size)
        """
        self.names = np.array(names)
        self.dim = len(names)
        self.name = 'default'
        self.sort_name = sort_name
        if sort_name is not None:
            self.sort_sel = np.where(self.names==sort_name)[0]
            self.sort_range = sort_range
        if logger is None:
            logger = init_logger()
        self.logger = logger
            
    def get_cov(self, chain):
        """ Return covariance SVD decomposition. 
        """
        return chain.U, chain.S 

    def sort_by(self, x):
        if self.sort_name is None:
            return x
        short_a = np.argsort(x[self.sort_sel])
        reshaped = x[self.sort_range[0]:].reshape(-1,self.sort_range[1])
        reshaped = reshaped[short_a,:]
        x = np.hstack([x[0:self.sort_range[0]], reshaped.flatten()])
        return x

    def history(self):
        return dict()
        
class Slice(Proposal):
    """ A slice sampler. 
    
    Any proposed points is accepted here. 
    """
    def __init__(self, names, **kwargs):
        """ Set scaling probability and factor. 
        """
        super().__init__(names, **kwargs)
        self.p1 = [0.95, 10.]
        self.p2 = [0.9, 0.2]
        self.jump = [0.2, 3] # prob, sigma
        self.max_cnt = 200
        self.name = 'slice'
        self.cnt = []
        
    def get_direction(self, x, U, S):
        """ Design the direction in which we move. 
        """
        prob = np.random.rand()
        if prob > self.p1[0]:
            scale = self.p1[1]
        elif prob > self.p2[0]:
            scale = self.p2[1]
        else:
            scale = 1.0
            
        d = len(x)
        cd = scale*2.38 /np.sqrt(d)
        dx  = np.dot(U, np.random.randn(d)*cd*np.sqrt(S))
        
        if (prob <= self.jump[0]): ### jump in the coordinate direction
            ix = np.random.choice(d)  ### choosing the coordinate
            del_x = self.jump[1]*dx[ix] ### choose 3 sigma jump in that coord. direction
            dx = np.zeros(d)
            dx[ix] = del_x
        return dx

    def slice(self, x, chain=None, **kwargs):
        """ Return actual sample.  
        
        Args:
        x: the current position
        chain: all additional runtime data needed to propose a new point. 
        
        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        U, S = self.get_cov(chain)
        dx = self.get_direction(x, U, S)
        logLxT = chain.Lx*chain.beta
        logu = logLxT - np.random.exponential(1.0)
        
        xr = np.copy(x)
        for i in range(self.max_cnt): # going "right"
            xr = xr + dx
            loglik = chain.log_l(xr, T=1/chain.beta)*chain.beta
            if loglik <= logu:
                break
        self.nl_cnt = i

        xl = np.copy(x)
        for i in range(self.nl_cnt, self.max_cnt): # going "left"
            xl = xl - dx
            loglik = chain.log_l(xl, T=1/chain.beta)*chain.beta
            if loglik <= logu:
                break
        self.nl_cnt = i

        for i in range(self.nl_cnt, self.max_cnt): # choosing a point along that direction
            al1 = np.random.random()
            al2 = np.random.random()
            if (al1 >= 0.5): # moving right
                xp = (xr - x)*al2 + x
                loglik = chain.log_l(xp, T=1/chain.beta)*chain.beta
                if loglik > logu:
                    pars = xp
                    break
                xr = np.copy(xp) # adjust the right boundary
            else: #moving left
                xp = (x - xl)*al2 + xl
                loglik = chain.log_l(xp, T=1/chain.beta)*chain.beta
                if loglik > logu:
                    pars = xp
                    break
                xl = np.copy(xp) # adjust the left boundary
        self.nl_cnt = i
        self.cnt.append(i)
        if self.nl_cnt >= self.max_cnt-1:
            return x, 1, chain.Lx, 0
        pars = self.sort_by(pars)
        return pars, 1, loglik/chain.beta, 0


    def history(self):
        return dict({"slice_cnt":self.cnt})
    
    
class SCAM(Proposal):
    """ A Single Component Adaptive Metropolis sampler. 
    """
    def __init__(self, names, **kwargs):
        """ Set scaling probability and factor. 
        """
        super().__init__(names, **kwargs)
        self.p1 = (0.97,10.)
        self.p2 = (0.90,0.2)
        self.addNoise = False
        self.name = 'SCAM'
        
    def SCAM(self, x, chain=None, **kwargs):
        """ Return actual sample by jumping in one component direction.  
        
        Args:
        x: the current position
        chain: all additional runtime data needed to propose a new point. 
        
        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        prob = np.random.rand()
        if prob>self.p1[0]: # ocasional large/small jump:
            scale = self.p1[1]
        elif prob>self.p2[0]:
            scale = self.p2[1]
        else:
            scale = 1.0

        d = len(x)
        U, S = self.get_cov(chain)
        cd = 2.38 * scale /np.sqrt(d)
        ind = np.unique(np.random.randint(0, self.dim, 1))
        x_new = x + np.random.randn()*cd* np.sqrt(S[ind]) * U[:,ind].flatten()
        x_new = self.sort_by(x_new)
        if self.addNoise:
            dx = 0.05*np.random.normal(0.0, 1.e-6/self.dim, self.dim)
            x_new = 0.95*x_new + dx

        return x_new, 0, None, 0

class ReMHA(Proposal):
    """ A Regional Metropolis Hastings Algorithm sampler. 
    """
    def __init__(self, names, **kwargs):
        """ Set scaling probability and factor. 
        """
        super().__init__(names, **kwargs)
        self.name = 'ReMHA'
        
    def ReMHA(self, x, chain=None, **kwargs):
        """ Return actual sample by jumping in one component direction.  
        
        Args:
        x: the current position
        chain: all additional runtime data needed to propose a new point. 
        
        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        d = len(x)
        if not chain.modes:
            chain.update_modes()
        Nm = len(chain.modes)
        means = np.array([md[0] for md in chain.modes])
        covs = np.array([md[1] for md in chain.modes])
        weights = np.array([md[2] for md in chain.modes])
        
        ## draw randomly from iy mode
        iy = np.random.choice(len(weights), p=weights)
        mn_y = np.array(means[iy, :])
        cv_y = 2.38**2 * np.array(covs[iy, :, :])/d
        y = np.random.multivariate_normal(mn_y, cv_y)
        y = self.sort_by(y)
        return y, 0, None, 0


    
class DE(Proposal):
    """ A differential evolution sampler. 
    """ 
    def __init__(self, names, DE_skip=1000, **kwargs):
        """ Set scaling probability and factor. 
        """
        super().__init__(names, **kwargs)
        self.DE_skip = DE_skip
        self.p = (0.5,1.0)
        self.pc = 0.7
        self.name = 'DE'
        
    def DE(self, x, chain=None, **kwargs):
        """ Return actual sample using differential evolution of a given chain.
        
        Args:
        x: the current position
        chain: all additional runtime data needed to propose a new point. 
        
        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        burn = self.DE_skip
        chain_size = chain.get_size()
        if (chain_size <= burn + 5):
            return x, -1, None, 0

        mm = np.random.randint(burn, chain_size)
        nn = np.random.randint(burn, chain_size)
        while mm == nn:
            nn = np.random.randint(burn, chain_size)

        scale = self.get_scale(chain)
        dx = chain.get_sample(mm) - chain.get_sample(nn)
        x_new = x + dx*scale
        x_new = self.sort_by(x_new)
        return x_new, 0, None, 0

    def get_scale(self, chain):
        """
        """
        prob = np.random.rand()
        ## choose scale of the jump
        if (prob>self.p[0]):
            scale = self.p[1]
        else:
            scale = np.random.rand() * 2.4 / np.sqrt(self.dim)*np.sqrt(chain.anneal/chain.beta)
        return scale
            
    def DE_all(self, x, chains=None, chain=None, **kwargs):
        """ Return actual sample using differential evolution of all chains.
        
        Args:
        x: the current position
        chains, chain: all additional runtime data needed to propose a new point. 

        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        burn = self.DE_skip
        ci1, ci2 = np.random.randint(0, len(chains), size=2) ## mixing all chains
        chain_size1 = len(chains[ci1].chn)
        chain_size2 = len(chains[ci2].chn)
        if chain_size1 <= burn + 5 or chain_size2 <= burn + 5:
            return x, -1, None, 0

        # we will use last 30% of each chain
        imin1 = max(burn, int(chain_size1*self.pc))
        imin2 = max(burn, int(chain_size2*self.pc))
        mm = np.random.randint(imin1, chain_size1)
        nn = np.random.randint(imin2, chain_size2)
        scale = self.get_scale(chain)

        dx = chains[ci1].get_sample(mm) - chains[ci2].get_sample(nn)
        x_new = x + dx*scale
        x_new = self.sort_by(x_new)
        return x_new, 0, None, 0



class AdaptiveKDE(Proposal):
    """ Adaptive KDE proposal base on hypKDE library
    """

    def __init__(self, names, **kwargs):
        """ Check that hyperkde is installed. 
        """
        if HyperKDE is None:
            print("ImportError: hyperkde is not installed.")
            
        super().__init__(names, **kwargs)
        self.name = 'adaptKDE'
        
    def kde_jump(self, x, chain, ims=0, **kwargs):
        """ Return new sample draw from KDE distribution. 
        """
        if chain.kde is None:
            return x, -1, None, 0

        x_new, qxy = chain.kde.draw_from_random_hyp_kde(x)
        return x_new, 0, None, qxy


class Prior(Proposal):
    """ A simple sampler based on priors. 
    """
    
    def __init__(self, names, prior, **kwargs):
        """ Set prior range. 
        """
        super().__init__(names, **kwargs)
        self.prior = np.array(prior)
        self.name = 'prior'
        
    def sample_prior(self, x, chain=None, **kwargs):
        """ Return actual sample. 
        
        Args:
        x: the current position
        chain: all additional runtime data needed to propose a new point. 
        
        Returns:
        y: the new position
        status: 0 (do MH decision), 1 (accept) or -1 (reject)
        logy: the log-likelihood at y position if already computed. 
        qxy: 0 for symmetric proposal distribution
        """
        sz = np.shape(self.prior)[0]
        y = np.random.random(sz)
        for i in range(sz):
            y[i] = y[i]*(self.prior[i,1] - self.prior[i,0]) +self. prior[i,0]
        y = self.sort_by(y)
        return y, 0, None, 0
