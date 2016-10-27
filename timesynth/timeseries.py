import numpy as np

__all__ = ['TimeSeries']


class TimeSeries:
    """TimeSeries class
    
    A TimeSeries object is the main interface from which to sample time series.
    You have to provide at least a signal generator; a noise generator is optional.
    It is recommended to set the sampling frequency.
    
    Parameters
    ----------
    signal_generator : Signal` object
        signal type for time series
    noise_generator : `Noise` object
        noise type for time series
    sampling_frequency : float or int
        how often the time series is sampled
    
    """
    def __init__(self, signal_generator, noise_generator=None, sampling_frequency=1):
        self.signal_generator = signal_generator
        self.noise_generator = noise_generator
        self.sampling_frequency = sampling_frequency

        # Set frequencies
        self.signal_generator.set_frequency(self.sampling_frequency)
        if not self.noise_generator is None:
            self.noise_generator.set_frequency(self.sampling_frequency)
            
    def sample_at_times(self, times):
        """
        
        """
        # ...

    def sample_(self, n_samples):
        
        # Vectorize if possible
        if self.signal_generator.vectorizable and not self.noise_generator is None and self.noise_generator.vectorizable:
            samples = signal_generator.sample_vectorized(n_samples)
            errors = noise_generator.sample_vectorized(n_samples)
            signals = samples + errors
            times = np.arange(n_samples)
        else:
            samples = np.zeros(n_samples)  # Signal and errors combined
            signals = np.zeros(n_samples)  # Signal samples
            errors = np.zeros(n_samples)  # Handle errors seprately
            times = np.arange(n_samples)

            # Sample iteratively, while providing access to all previously sampled steps
            for i in range(n_samples):
                
                # Get time
                t = times[i]
                
                # Sample error
                if not self.noise_generator is None:
                    errors[i] = self.noise_generator.sample_next(t, samples[:i - 1], errors[:i - 1])
                    
                # Sample signal
                signal = self.signal_generator.sample_next(t, samples[:i - 1], errors[:i - 1])
                signals[i] = signal
                
                # Compound signal and noise
                samples[i] = signals[i] + errors[i]
        
        # Return both times and samples, as well as signals and errors
        return times, samples, signals, errors

    def sample_range(self, start, stop, step):
        num_samples = (stop - start) // step
        return self.sample(num_samples, step)
