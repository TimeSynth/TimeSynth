import pytest
import timesynth as ts


def run_test():
    time_sampler = ts.TimeSampler(stop_time=20)
    irregular_time_samples = time_sampler.sample_irregular_time(num_points=500, keep_percentage=50)
    dde = ts.signals.MackeyGlass()
    samples = dde.sample_vectorized(irregular_time_samples)
    single_sample = dde.sample_next(irregular_time_samples[0], None, None)
    return samples, single_sample


def test_dde():
    samples, single_sample = run_test()
    assert len(samples) == 250
