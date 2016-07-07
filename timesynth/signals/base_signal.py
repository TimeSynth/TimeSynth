class BaseSignal:
    """BaseSignal class
    Signature for all signal classes.
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def sample_next(self, samples, errors):
        raise NotImplementedError
        
    def set_frequency(self, frequency):
        raise NotImplementedError
