import warnings
import numpy as np
from .base_signal import BaseSignal
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from jitcdde import y, t, jitcdde


__all__ = ['MackeyGlass']


class MackeyGlass(BaseSignal):
    """Signal generator for the Mackey-Glass delay differential equation (DDE).

    The Mackey-Glass DDE is defined as follows:
    .. math::

        \\frac{dx}{dt} = \\beta \\frac{ x_{\\tau} }{1+{x_{\\tau}}^n}-\\gamma x,
        \\quad \\gamma,\\beta,n > 0,
        x_{\\tau} = x(t - \\tau)

    Chaotic behavior may occur for tau >= 17.

    Parameters
    ----------
    tau : float (default 17)
        The delay parameter
    n : float (default 10)
        The parameter n
    beta : float (default 0.2)
        The parameter beta
    gamma : float (default 0.1)
        The parameter gamma
    initial_condition : array-like or None (default None)
        A 2-D array consisting of entries in the form (time, value, derivative)
        to be used as an inital condition on the DDE. If set to None a default
        will be used.
    burn_in : float (default 500)
        Amount of time after which samples will be taken and returned

    """

    def __init__(self, tau=17., n=10., beta=0.2, gamma=0.1, initial_condition=None, burn_in=500):
        self.vectorizable = True

        # Set system of equations
        f = [- gamma * y(0) + beta * y(0, t-tau) / (1.0 + y(0, t-tau) ** n)]
        self.dde = jitcdde(f)

        # Set initial condition
        if initial_condition is None:
            y_initial = 0.5
            dy = lambda y: -gamma * y + beta * y / (1.0 + y ** n)
            dy_initial = dy(y_initial)
            self.dde.add_past_point(0.0, np.array([y_initial]), np.array([dy_initial]))
            self.dde.add_past_point(tau, np.array([1.0]), np.array([0.0]))
        else:
            for condition in initial_condition:
                time, value, derivative = condition
                self.dde.add_past_point(time, np.array([value]), np.array([derivative]))

        # Prepare DDE
        self.dde.generate_lambdas()
        self.dde.set_integration_parameters()

        # Run burn_in
        self.burn_in = burn_in
        self.dde.integrate_blindly(self.burn_in)

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
        return self.dde.integrate(self.burn_in + time)

    def sample_vectorized(self, time_vector):
        """Samples for all time points in input

        Parameters
        ----------
        time_vector : array like
            all time stamps to be sampled

        Returns
        -------
        numpy array
            samples for times provided in time_vector

        """
        samples = []
        for t in time_vector:
            samples.append(self.dde.integrate(self.burn_in + t))
        return np.array(samples).reshape(-1,)
