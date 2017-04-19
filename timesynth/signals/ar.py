import numpy as np
from .base_signal import BaseSignal

__all__ = ['AutoRegressive']


class AutoRegressive(BaseSignal):
    """Sample generator for autoregressive (AR) signals.
    
    Generates time series with an autogressive lag defined by the number of parameters in ar_param.
    NOTE: Only use this for regularly sampled signals
    
    Parameters
    ----------
    ar_param : list (default [None])
        Parameter of the AR(p) process
        [phi_1, phi_2, phi_3, .... phi_p]
    sigma : float (default 1.0)
        Standard deviation of the signal
    start_value : list (default [None])
        Starting value of the AR(p) process
        
    """
    
    def __init__(self, ar_param=[None], sigma=0.5, start_value=[None]):
        self.vectorizable = False
        ar_param.reverse()
        self.ar_param = ar_param
        self.sigma = sigma
        if start_value[0] is None:
            self.start_value = [0 for i in range(len(ar_param))]
        else:
            if len(start_value) != len(ar_param):
                raise ValueError("AR parameters do not match starting value")
            else:
                self.start_value = start_value
        self.previous_value = self.start_value

    def sample_next(self, time, samples, errors):
        """Sample a single time point

        Parameters
        ----------
        time : number
            Time at which a sample was required

        Returns
        -------
        ar_value : float
            sampled signal for time t
        """
        ar_value = [self.previous_value[i] * self.ar_param[i] for i in range(len(self.ar_param))]
        noise = np.random.normal(loc=0.0, scale=self.sigma, size=1)
        ar_value = np.sum(ar_value) + noise
        self.previous_value = self.previous_value[1:]+[ar_value]
        return ar_value
