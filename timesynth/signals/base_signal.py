__all__ = []


class BaseSignal:
    """BaseSignal class

    Signature for all signal classes.

    """

    def __init__(self):
        raise NotImplementedError

    def sample_next(self, time, samples, errors):
        """Samples next point based on history of samples and errors

        Parameters
        ----------
        time : int
            time
        samples : array-like
            all samples taken so far
        errors : array-like
            all errors sampled so far

        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError

    def sample_vectorized(self, time_vector):
        """Samples for all time points in input

        Parameters
        ----------
        time_vector : array like
            all time stamps to be sampled
        
        Returns
        -------
        float
            sampled signal for time t

        """
        raise NotImplementedError
