class BaseSignal:
    """BaseSignal class
    Signature for all signal classes.
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def sample_next(self, t, samples, errors): # We provide t for irregularly sampled timeseries
        raise NotImplementedError
        
    def set_frequency(self, frequency):
        raise NotImplementedError
