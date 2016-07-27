import numpy as np
from .base_signal import BaseSignal

__all__ = ['PseudoPeriodic']


class PseudoPeriodic(BaseSignal):

    def __init__(self, amplitude=1.0, frequency=100, ampSD=0.1, freqSD=0.4):
        self.amplitude = amplitude
        self.frequency = frequency
        self.freqSD = freqSD
        self.ampSD = ampSD
        self.setFreqLow = False

    def sample_next(self, t, samples, errors):
        self.curr_sample += self.resolution
        freqVal = np.random.normal(loc=self.frequency, scale=self.freqSD, size=1)
        amplitudeVal = np.random.normal(loc=self.amplitude, scale=self.ampSD, size=1)
        return float(amplitudeVal * np.sin(freqVal * self.curr_sample)), self.curr_sample

    def sample(self, nsamples=100):
        timeVec = np.linspace(0, nsamples * self.resolution, num=nsamples)
        freqArr = np.random.normal(loc=self.frequency, scale=self.freqSD, size=nsamples)
        ampArr = np.random.normal(loc=self.amplitude, scale=self.ampSD, size=nsamples)
        signal = np.multiply(ampArr, np.sin(np.multiply(freqArr, timeVec)))
        return signal, timeVec

    def set_frequency(self, frequency):
        self.resolution = 1. / frequency
        self.curr_sample = -self.resolution
