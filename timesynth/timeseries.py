class TimeSeriesGenerator:
    def __init__(self, sampling_frequency, signal_generator, noise_generator):
        self.sampling_frequency = sampling_frequency
        self.signal_generator = signal_generator
        self.noise_generator = noise_generator

        # Set frequencies
        self.signal_generator.set_frequency(self.sampling_frequency)
        self.noise_generator.set_frequency(self.sampling_frequency)

    def sample(self, n_samples):
        samples = np.zeros(n_samples)  # Signal and errors combined
        signals = np.zeros(n_samples)  # Signal samples
        errors = np.zeros(n_samples)  # Handle errors seprately

        # Sample iteratively, while providing access to all previously sampled steps
        for i in range(n_samples):
            signals[i] = self.signal_generator.sample_next(samples[:i - 1], errors[:i - 1])
            errors[i] = self.noise_generator.sample_next(samples[:i - 1], errors[:i - 1])
            samples[i] = signals[i] + errors[i]
        
        # Only return samples
        return samples

    def sample_range(self, start, stop, step):
        num_samples = (stop - start) // step
        return self.sample(num_samples, step)
