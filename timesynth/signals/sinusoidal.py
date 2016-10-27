import numpy as np
from .base_signal import BaseSignal


__all__ = ['Sinusoidal']


class Sinusoidal(BaseSignal):

    def __init__(self, amplitude=1.0):
        self.vectorizable = True
        self.amplitude = amplitude

    def sample_next(self, t, samples, errors):
        self.current_sample += self.resolution
        return self.amplitude * self.ftype(self.curr_sample), self.curr_sample

    def sample_vectorized(self, n_samples=100):
        timeVec = np.linspace(0, n_samples * self.resolution, num=n_samples)
        signal = self.amplitude * self.ftype(timeVec)

        return signal, timeVec

    def set_frequency(self, frequency):
        self.resolution = 1. / frequency
        self.curr_sample = -self.resolution
        self.setFreqFlag = True
