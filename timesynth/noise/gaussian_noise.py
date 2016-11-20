import numpy as np
from .base_noise import BaseNoise


__all__ = ['GaussianNoise']


class GaussianNoise(BaseNoise):
    """Gaussian noise generator.
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

    def sample_next(self, t, samples, errors):
        return np.random.normal(loc=self.mean, scale=self.std, size=1)

    def sample_vectorized(self, time_vector):
        n_samples = len(time_vector)
        return np.random.normal(loc=self.mean, scale=self.std, size=n_samples)
