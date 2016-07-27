import numpy as np
from .base_signal import BaseSignal

__all__ = ['GaussianProcess']


class GaussianProcess(BaseSignal):
    """Gaussian Process sampler
    
    Attributes
    ----------
    amplitude : float
        desc
    length_scale : float
        the characteristic length scale used to generate the covariance matrix
    kernel : string
        the kernel type, which can be `exponential`, `linear` or `matern`
        
    """

    def __init__(self, amplitude=1.0, length_scale=20, kernel="exponential"):
        self.amplitude = amplitude
        self.kernel_options = {"exponential": np.exp, "linear": lambda x: x, "matern": None}  # TODO
        self.kernel_function = self.kernel_options[kernel]
        self.length_scale = length_scale

    def sample_next(self, t, samples, errors):
        return NotImplementedError

    def sample(self, n_samples=100):
        times = np.linspace(0, n_samples * self.resolution, num=n_samples)
        mean = np.zeros(n_samples)
        samples = np.array([[j for j in range(n_samples)] for k in range(n_samples)])
        covariance_matrix = self.kernel_function(-(vec - vec.T)**2 / float(self.length_scale**2))
        signal = self.amplitude * np.random.multivariate_normal(mean, covMat, size=(1,))[0]
        return signal, timeVec

    def set_frequency(self, frequency):
        self.resolution = 1. / frequency
        self.curr_sample = -self.resolution
