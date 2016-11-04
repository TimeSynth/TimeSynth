import numpy as np
from .base_signal import BaseSignal

__all__ = ['CAR']


class CAR(BaseSignal):

    def __init__(self, ar_param=1.0, sigma=0.5, start_value=0.01):
        """Initialize Continuous Autoregressive class

        Parameters
        ----------
        ar_param : number (default 1.0)
            Parameter of the AR(1) process
        sigma : number (default 1.0)
            Standard deviation of the signal
        start_value : number (default 0.0)
            Starting value of the AR process
        """
        self.vectorizable = False
        self.ar_param = ar_param
        self.sigma = sigma
        self.start_value = start_value
        self.previous_value = None
        self.previous_time = None

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
        if self.previous_value is None:
            output = self.start_value
        else:
            time_diff = time - self.previous_time
            noise = np.random.normal(loc=0.0, scale=1.0, size=1)
            output = (np.power(self.ar_param, time_diff))*self.previous_value+\
                self.sigma*np.sqrt(1-np.power(self.ar_param, time_diff))*noise
        self.previous_time = time
        self.previous_value = output
        return output
