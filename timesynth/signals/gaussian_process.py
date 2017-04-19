import numpy as np
import scipy.special
from .base_signal import BaseSignal

__all__ = ['GaussianProcess']


class GaussianProcess(BaseSignal):
    """Gaussian Process time series sampler
    
    Samples time series from Gaussian Process with selected covariance function (kernel).

    Parameters
    ----------
    kernel : {'SE', 'Constant', 'Exponential', 'RQ', 'Linear', 'Matern', 'Periodic'}
        the kernel type, as described in [1]_ and [2]_, which can be:
        
        - `Constant`. All covariances set to `variance`
        - `Exponential`. Ornstein-Uhlenbeck kernel. Optionally, set keyword `gamma` for a gamma-exponential kernel
        - `SE`, the squared exponential.
        - `RQ`, the rational quadratic. To use this kernel, set keyword argument `alpha`
        - `Linear`. To use this kernel, set keyword arguments `c` and `offset`
        - `Matern`. To use this kernel, set keyword argument `nu`
        - `Periodic`. To use this kernel, set keyword argument `p` for the period
        
    mean : float
        the mean of the gaussian process
    variance : float
        the output variance of the gaussian process (sigma^2)
    lengthscale : float
            the characteristic lengthscale used to generate the covariance matrix
    
    References
    ----------
    .. [1] URL: http://www.cs.toronto.edu/~duvenaud/cookbook/index.html
    .. [2] Rasmussen, C.E., 2006. Gaussian processes for machine learning. URL: https://pdfs.semanticscholar.org/a9fe/ab0fe858dbde2eecff8b1f7c629cc6aff8ad.pdf

    """

    def __init__(self, kernel="SE", lengthscale=1., mean=0., variance=1., c=1., gamma=1., alpha=1., offset=0., nu=5./2, p=1.):
        self.vectorizable = True
        self.lengthscale = lengthscale
        self.mean = mean
        self.variance = variance
        self.kernel = kernel
        self.kernel_function = {"Constant": lambda x1, x2: variance,
                                "Exponential": lambda x1, x2: variance * np.exp(-np.power(np.abs(x1 - x2) / lengthscale, gamma)),
                                "SE": lambda x1, x2: variance * np.exp(- np.square(x1 - x2) / (2 * np.square(lengthscale))),
                                "RQ": lambda x1, x2: variance * np.power((1 + np.square(x1 - x2) / (2 * alpha * np.square(lengthscale))), -alpha),
                                "Linear": lambda x1, x2: variance * (x1 - c) * (x2 - c) + offset,
                                "Matern": lambda x1, x2: variance if x1 - x2 == 0. else variance * (np.power(2, 1 - nu) / scipy.special.gamma(nu)) * np.power(np.sqrt(2 * nu) * np.abs(x1 - x2) / lengthscale, nu) * scipy.special.kv(nu, np.sqrt(2 * nu) * np.abs(x1 - x2) / lengthscale),
                                "Periodic":lambda x1, x2: variance * np.exp(- 2 * np.square(np.sin(np.pi * np.abs(x1 - x2) / p))),
                                }[kernel]

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
        raise NotImplementedError

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
        cartesian_time = np.dstack(np.meshgrid(time_vector, time_vector)).reshape(-1, 2)
        covariance_matrix = (np.vectorize(self.kernel_function)(cartesian_time[:, 0], cartesian_time[:, 1])).reshape(-1, time_vector.shape[0])
        covariance_matrix[np.diag_indices_from(covariance_matrix)] += 1e-12  # Add small value to diagonal for numerical stability
        return np.random.multivariate_normal(mean=np.full(shape=(time_vector.shape[0],), fill_value=self.mean), cov=covariance_matrix)
