class TimeSeries:
    
    def __init__(self, signal, noise):
        self.signal = signal
        self.noise = noise
        raise NotImplementedError
    
    def sample(n_samples):
        self.samples = np.zeros(n_samples)
        self.errors = np.zeros(n_samples)
        raise NotImplementedError
