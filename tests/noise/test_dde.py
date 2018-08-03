import pytest
import timesynth as ts


def run_test():
    time_sampler = ts.TimeSampler(stop_time=20)
    irregular_time_samples = time_sampler.sample_irregular_time(num_points=500, keep_percentage=50)
    dde = ts.signals.MackeyGlass()
    wnoise_vec = dde.sample_vectorized(irregular_time_samples)
    wnoise_value = dde.sample_next(irregular_time_samples[0],
                                           None, None)
    return wnoise_vec, wnoise_value


def test_dde():
    wnoise_vec, wnoise_value = run_test()
    assert len(wnoise_vec) == 250
