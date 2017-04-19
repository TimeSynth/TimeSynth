import numpy as np
from .base_signal import BaseSignal

__all__ = ['NARMA']


class NARMA(BaseSignal):
    """Non-linear Autoregressive Moving Average generator.
    
    An n-th order signal generator of the NARMA class, as defined in [1]_:
    .. \math:: y(k+1) = a[0] * y(k) + a[1] * y(k) * \sum_{i=0}^{n-1} y(k-i) + a[2] * u(k-(n-1)) * u(k) + a[3]
    
    where u is generated from Uniform(0, 0.5).
    
    NOTE: Only supports regular time samples.
    
    Parameters
    ----------
    order : int (default 10)
        The order (n) of non-linear interactions as described in the formula above.
    coefficients : iterable (default [0.3, 0.05, 1.5, 0.1])
        The coefficients denoted by iterable `a` in the formula above. As in [1]_.
    initial_condition : iterable or None (default None)
        An array of starting values of y(k-n) until y(k). The default is an aray of zeros.
    
    
    References
    ----------
    .. [1] http://ieeexplore.ieee.org.ezp-prod1.hul.harvard.edu/stamp/stamp.jsp?arnumber=846741
    
    """
    
    def __init__(self, order=10, coefficients=[0.3, 0.05, 1.5, 0.1], initial_condition=None):
        self.vectorizable = True
        self.order = order
        self.coefficients = np.array(coefficients)
        if not initial_condition is None:
            self.initial_condition = np.array(initial_condition)
        else:
            self.initial_condition = np.zeros(order)
        
    
    def _next_value(self, values, rands, index):
        """Internal short-hand method to calculate next value."""
        # Short-hand parameters
        n = self.order
        a = self.coefficients
        
        # Get value arrays
        i = index
        y = values
        u = rands
        
        # Compute next value
        return a[0] * y[i-1] + a[1] * y[i-1] * np.sum(y[i-n:n]) + a[2] * u[i-n] * u[i] + a[3]
        
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
        raise NotImplementedError('NARMA can only be sampled vectorized. \
                                   Remove or replace error function')

    def sample_vectorized(self, times):
        """Samples for all time points in input

        Parameters
        ----------
        times: array like
            all time stamps to be sampled
        
        Returns
        -------
        samples : numpy array
            samples for times provided in time_vector

        """
        # Set bounds
        start = self.initial_condition.shape[0]
        
        # Get relevant arrays
        inits = self.initial_condition
        rands = np.random.uniform(0, .5, size=start + times.shape[0])
        values = np.concatenate((inits, np.zeros(times.shape[0])))
        
        # Sample step-wise
        end = values.shape[0]
        for t in range(start, end):
            values[t] = self._next_value(values, rands, t)
        
        # Return trimmed values (exclude initial condition)
        samples = values[start:]
        return samples
