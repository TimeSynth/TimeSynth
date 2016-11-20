import warnings
import numpy as np
from .base_signal import BaseSignal
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from jitcdde import provide_advanced_symbols, jitcdde


__all__ = ['DDE', 'MackeyGlass']


class DDE(BaseSignal):
    """Sample generator for delay differential equations

    Parameters
    ----------
    

    """
    
    def __init__(self):
        pass
    
    def sample_next(self, time, samples, errors):
        """Samples next point based on history of samples and errors

        Parameters
        ----------
        time : int
            time
        samples : array-like
            all samples taken so far
        errors : array-like
            all errors sampled so far

        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError

    def sample_vectorized(self, time_vector):
        """Samples for all time points in input

        Parameters
        ----------
        time_vector : array like
            all time stamps to be sampled
        
        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError



class MackeyGlass(DDE):
    def __init__(self):
        super().__init__
        pass
    
    def sample_next(self, time, samples, errors):
        """Samples next point based on history of samples and errors

        Parameters
        ----------
        time : int
            time
        samples : array-like
            all samples taken so far
        errors : array-like
            all errors sampled so far

        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError

    def sample_vectorized(self, time_vector):
        """Samples for all time points in input

        Parameters
        ----------
        time_vector : array like
            all time stamps to be sampled
        
        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError

        
