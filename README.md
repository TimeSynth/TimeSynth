[![Build Status](https://travis-ci.org/TimeSynth/TimeSynth.svg?branch=master)](https://travis-ci.org/TimeSynth/TimeSynth) [![codecov](https://codecov.io/gh/TimeSynth/TimeSynth/branch/master/graph/badge.svg)](https://codecov.io/gh/TimeSynth/TimeSynth)

# TimeSynth
_Multipurpose Library for Synthetic Time Series_

**TimeSynth** is an open source library for generating synthetic time series for
model testing. The library can generate regular and irregular time series. The architecture
allows the user to match different signals with different architectures allowing
a vast array of signals to be generated. The available signals and noise types are
listed below.

N.B. We only support Python 3.5+ at this time.

#### Signal Types
* Harmonic functions(sin, cos or custom functions)
* Gaussian processes with different kernels
    * Constant
    * Squared exponential
    * Exponential
    * Rational quadratic
    * Linear
    * Matern
    * Periodic
* Pseudoperiodic signals
* Autoregressive(p) process
* Continuous autoregressive process (CAR)
* Nonlinear Autoregressive Moving Average model (NARMA)

#### Noise Types
* White noise
* Red noise

### Installation
To install the package via github,
```{bash}
git clone https://github.com/TimeSynth/TimeSynth.git
cd TimeSynth
python setup.py install
```

### Using TimeSynth
```shell
$ python
```
The code snippet demonstrates creating a irregular sinusoidal signal with white noise.
```python
>>> import timesynth as ts
>>> # Initializing TimeSampler
>>> time_sampler = ts.TimeSampler(stop_time=20)
>>> # Sampling irregular time samples
>>> irregular_time_samples = time_sampler.sample_irregular_time(num_points=500, keep_percentage=50)
>>> # Initializing Sinusoidal signal
>>> sinusoid = ts.signals.Sinusoidal(frequency=0.25)
>>> # Initializing Gaussian noise
>>> white_noise = ts.noise.GaussianNoise(std=0.3)
>>> # Initializing TimeSeries class with the signal and noise objects
>>> timeseries = ts.TimeSeries(sinusoid, noise_generator=white_noise)
>>> # Sampling using the irregular time samples
>>> samples, signals, errors = timeseries.sample(irregular_time_samples)
```
