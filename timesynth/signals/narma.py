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
    seed : int
        Use this seed to recreate any of the internal errors.
        
    Attributes
    ----------
    errors : numpy array or None
        Random number sequence that was used to generate last NARMA sequence.
    
    References
    ----------
    .. [1] http://ieeexplore.ieee.org.ezp-prod1.hul.harvard.edu/stamp/stamp.jsp?arnumber=846741
    
    """
    
    def __init__(self, order=10, coefficients=[0.3, 0.05, 1.5, 0.1], initial_condition=None,
                 error_initial_condition=None, seed=42):
        self.vectorizable = True
        self.order = order
        self.coefficients = np.array(coefficients)
        self.random = np.random.RandomState(seed)
        
        # Store initial conditions
        if initial_condition is None:
            self.initial_condition = np.zeros(order)
        else:
            self.initial_condition = np.array(initial_condition)
        
        # You may provide an error initial condition
        if error_initial_condition is None:
            self.error_initial_condition = self.random.uniform(0, 0.5, size=order)
        else:
            self.error_initial_condition = error_initial_condition
        
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
        """This method is not available for NARMA, due to internal error sampling."""
        raise NotImplementedError("NARMA can only be sampled vectorized.")
        
    def sample_vectorized(self, times):
        """Samples for all time points in input
        
        Internalizes Uniform(0, 0.5) random distortion for u.

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
        rand_inits = self.error_initial_condition
        rands = np.concatenate((rand_inits, self.random.uniform(0, .5, size=times.shape[0])))
        values = np.concatenate((inits, np.zeros(times.shape[0])))
        
        # Sample step-wise
        end = values.shape[0]
        for t in range(start, end):
            values[t] = self._next_value(values, rands, t)
        
        # Store valus for later retrieval
        self.errors = rands[start:]
        
        # Return trimmed values (exclude initial condition)
        samples = values[start:]
        return samples
