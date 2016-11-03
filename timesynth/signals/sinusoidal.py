import numpy as np
from .base_signal import BaseSignal


__all__ = ['Sinusoidal']


class Sinusoidal(BaseSignal):

    def __init__(self, amplitude=1.0, frequency=1.0, ftype=np.sin):
        """Initialize Sinusoidal class

        Parameters
        ----------
        amplitude : number (default 1.0)
            Amplitude of the harmonic series
        frequency : number (default 1.0)
            Frequency of the harmonic series
        ftype : function (default np.sin)
            Harmonic function

        """
        self.vectorizable = True
        self.amplitude = amplitude
        self.ftype = ftype
        self.frequency = frequency

    def sample_next(self, time, samples, errors):
        """Sample a single time point

        Parameters
        ----------
        time : number
            Time at which a sample was required

        Returns
        -------
        float
            sampled signal for time t

        """
        return self.amplitude * self.ftype(2*np.pi*self.frequency*time)

    def sample_vectorized(self, time_vector):
        """Sample a single time point

        Parameters
        ----------
        time_vector : array-like
            Timestamps for signal generation

        Returns
        -------
        float
            sampled signal for time t

        """
        if self.vectorizable is True:
            signal = self.amplitude * self.ftype(2*np.pi*self.frequency *
                                                 time_vector)
            return signal
        else:
            raise ValueError("Signal type not vectorizable")
