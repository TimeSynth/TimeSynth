import numpy as np
from base_signal import BaseSignal
import warnings
warnings.filterwarnings("ignore")

class MultivariateGaussian(BaseSignal):

    def __init__(self, amplitude=1.0, L=20, kernel="exponential"):
        self.amplitude = amplitude
        self.setFreqFlag = False
        self.kernelOptions = {"exponential": np.exp, \
                                "linear": lambda x:x}
        self.kernelFunction = self.kernelOptions[kernel]
        self.L = L

    def sample_next(self, samples, errors):
        return NotImplementedError

    def sample(self, nsamples=100):

        assert self.setFreqFlag == True, "Frequency not set for MultivariateGaussian object"
        timeVec = np.linspace(0, nsamples*self.resolution, num=nsamples)
        mean = np.zeros(nsamples)
        vec = np.array([[j for j in range(0,nsamples)] for k in range(0,nsamples)])
        covMat = self.kernelFunction(-(vec - vec.T)**2/float(self.L**2))  
        signal = self.amplitude*np.random.multivariate_normal(mean, covMat, size=(1,))[0]

        return signal, timeVec

    def set_frequency(self, frequency):
        self.resolution = 1./frequency
        self.curr_sample = -self.resolution
        self.setFreqFlag = True


