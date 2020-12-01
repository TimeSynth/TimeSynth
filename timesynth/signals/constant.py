from .base_signal import BaseSignal


__all__ = ['Constant']


class Constant(BaseSignal):
    """Signal generator for constant value.

    Parameters
    ----------
    value : number (default 0.0)
        value of the signal

    """

    def __init__(self, value=0.0):
        self.vectorizable = True
        self.value = value

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
        return self.value

    def sample_vectorized(self, time_vector):
        """Sample entire series based off of time vector

        Parameters
        ----------
        time_vector : array-like
            Timestamps for signal generation

        Returns
        -------
        array-like
            sampled signal for time vector

        """
        if self.vectorizable is True:
            signal = [self.value] * len(time_vector)
            return signal
        else:
            raise ValueError("Signal type not vectorizable")
