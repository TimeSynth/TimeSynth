import numpy as np
from .base_noise import BaseNoise

class GaussianNoise(BaseNoise):

    def __init__(self, mean=0, std=0):
        """
        """
        self.mean = mean
        self.std = std

    def sample_next(self, samples, errors):
        return np.random.normal(loc=self.mean, scale=self.std, size=1)
    
    def set_frequency(self, frequency):
        pass

    def sample(self, nsamples):
        return np.random.normal(loc=self.mean, scale=self.std, size=nsamples)
