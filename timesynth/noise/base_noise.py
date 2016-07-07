class BaseNoise:
    """BaseNoise class
    Signature for all noise classes.
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def sample_next(self, samples, errors):
        raise NotImplementedError

    def set_frequency(self, frequency):
        raise NotImplementedError
