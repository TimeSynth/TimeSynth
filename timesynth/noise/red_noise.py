import numpy as np
from .base_noise import BaseNoise


__all__ = ['RedNoise']


class RedNoise(BaseNoise):
    """Red noise generator.
    This class adds correlated (red) noise to your signal.

    Attributes
    ----------
    mean : float
        mean for the noise
    std : float
        standard deviation for the noise
    tau : float
        ?
    start_value : float
        ?

    """

    def __init__(self, mean=0, std=1., tau=0.2, start_value=0):
        self.vectorizable = False
        self.mean = mean
        self.std = std
        self.start_value = 0
        self.tau = tau
        self.previous_value = None
        self.previous_time = None

    def sample_next(self, t, samples, errors):
        if self.previous_time is None:
            red_noise = self.start_value
        else:
            time_diff = t - self.previous_time
            wnoise = np.random.normal(loc=self.mean, scale=self.std, size=1)
            red_noise = ((self.tau/(self.tau + time_diff)) *
                         (time_diff*wnoise + self.previous_value))
        self.previous_time = t
        self.previous_value =red_noise
        return red_noise
