class TimeSeriesGenerator:
    
    def __init__(self, signal_generator, noise_generator):
        self.signal_generator = signal_generator
        self.noise_generator = noise_generator
    
    def sample(self, n_samples, resolution):
        samples = np.zeros(n_samples)  # Signal and errors combined
        signals = np.zeros(n_samples)  # Signal samples
        errors = np.zeros(n_samples)  # Handle errors seprately
        
        # Sample iteratively, while providing access to all previously sampled steps
        for i in range(n_samples):
            signals[i] = self.signal_generator.sample_next(samples[:i-1], errors[:i-1])
            errors[i] = self.noise_generator.sample_next(samples[:i-1], errors[:i-1])
            samples [i] = signals[i] + errors[i]
            
        return samples

    def sample_range(self, start, stop, step):
        num_samples = (stop - start) // step
        return self.sample(num_samples, step)
