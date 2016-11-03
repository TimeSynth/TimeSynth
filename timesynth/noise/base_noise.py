__all__ = []


class BaseNoise:
    """BaseNoise class

    Signature for all noise classes.

    """

    def __init__(self):
        raise NotImplementedError

    def sample_next(self, t, samples, errors):  # We provide t for irregularly sampled timeseries
        """Samples next point based on history of samples and errors

        Parameters
        ----------
        t : int
            time
        samples : array-like
            all samples taken so far
        errors : array-like
            all errors sampled so far

        Returns
        -------
        float
            sampled error for time t

        """
        raise NotImplementedError
