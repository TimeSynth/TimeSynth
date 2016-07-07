import numpy as np
from .base_signal import BaseSignal

class Sinusoidal():

    def __init__(self, amplitude=1.0, resolution=0.1):

        self.amplitude = amplitude
        self.resolution = resolution

        self.curr_sample = -resolution

    def sample_next(self, samples, errors):
        self.curr_sample += self.resolution
        return np.sin(self.curr_sample), self.curr_sample


    def sample(self, nsamples=100):
        timeVec = np.linspace(0, nsamples*self.resolution, num=nsamples)
        signal = np.sin(timeVec)

        return signal, timeVec

"""
if __name__ == "__main__":
    sig = Sinusoidal()
    print sig.sample(nsamples=10)
"""
