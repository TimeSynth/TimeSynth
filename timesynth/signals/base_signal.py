__all__ = []


class BaseSignal:
    """BaseSignal class
    
    Signature for all signal classes.
    
    Methods
    ------
    sample_next : ...
        ...
    
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def sample_next(self, t, samples, errors):
        """Samples next point based on history of samples and errors
        
        Parameters
        ----------
        t : int
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
        
    def set_frequency(self, frequency):
        raise NotImplementedError
