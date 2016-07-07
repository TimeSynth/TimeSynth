class BaseNoise:
    
    def __init__(self):
        raise NotImplementedError
    
    def sample_next(self, samples, errors):
        raise NotImplementedError
