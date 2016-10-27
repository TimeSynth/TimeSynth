import numpy as np
from .base_noise import BaseNoise


__all__ = ['GaussianNoise']


class GaussianNoise(BaseNoise):
    """Gaussian noise sampler
    
    This class adds uncorrelated, additive white noise to your signal.
    
    Attributes
    ----------
    mean : float
        mean for the noise
    std : float
        standard deviation for the noise
    
    """

    def __init__(self, mean=0, std=1.):
        self.vectorizable = True
        self.mean = mean
        self.std = std
        
    def set_frequency(self, frequency):
        pass  # Gaussian additive noise is independent of timing

    def sample_next(self, t, samples, errors):
        return np.random.normal(loc=self.mean, scale=self.std, size=1)

    def sample_vectorized(self, n_samples):
        return np.random.normal(loc=self.mean, scale=self.std, size=n_samples)
