import numpy as np


__all__ = ['TimeSampler']


class TimeSampler:
    """TimeSampler determines how and when samples will be taken from signal and noise.
    Samples timestamps for regular and irregular time signals

    Parameters
    ----------
    start_time: float/int (default 0)
                Time sampling of time series starts
    stop_time: float/int (default 10)
                Time sampling of time series stops

    """
    def __init__(self, start_time=0, stop_time=10):
        self.start_time = start_time
        self.stop_time = stop_time

    def sample_regular_time(self, num_points=None, resolution=None):
        """
        Samples regularly spaced time using the number of points or the
        resolution of the signal. Only one of the parameters is to be
        initialized. The resolution keyword argument is given priority.

        Parameters
        ----------
        num_points: int (default None)
            Number of points in time series
        resolution: float/int (default None)
            Resolution of the time series

        Returns
        -------
        numpy array
            Regularly sampled timestamps

        """
        if num_points is None and resolution is None:
            raise ValueError("One of the keyword arguments must be initialized.")
        if resolution is not None:
            time_vector = np.arange(self.start_time, self.stop_time,
                                    resolution)
            return time_vector
        else:
            time_vector = np.linspace(self.start_time, self.stop_time,
                                      num_points)
            return time_vector

    def sample_irregular_time(self, num_points=None, resolution=None,
                              keep_percentage=100):
        """
        Samples regularly spaced time using the number of points or the
        resolution of the signal. Only one of the parameters is to be
        initialized. The resolution keyword argument is given priority.

        Parameters
        ----------
        num_points: int (default None)
            Number of points in time series
        resolution: float/int (default None)
            Resolution of the time series
        keep_percentage: int(default 100)
            Percentage of points to be retained in the irregular series

        Returns
        -------
        numpy array
            Irregularly sampled timestamps

        """
        if num_points is None and resolution is None:
            raise ValueError("One of the keyword arguments must be initialized.")
        if resolution is not None:
            time_vector = np.arange(self.start_time, self.stop_time,
                                    resolution)
        else:
            time_vector = np.linspace(self.start_time, self.stop_time,
                                      num_points)
            resolution = float(self.stop_time-self.start_time)/num_points
        time_vector = self._select_random_indices(time_vector,
                                                  keep_percentage)
        return self._create_perturbations(time_vector, resolution)

    def _create_perturbations(self, time_vector, resolution):
        """
        Internal functions to create perturbations in timestamps

        Parameters
        ----------
        time_vector: numpy array
            timestamp vector

        resolution: float/int
            resolution of the time series

        Returns
        -------
        numpy array
            Irregularly sampled timestamps with perturbations

        """
        sample_perturbations = np.random.normal(loc=0.0, scale=resolution,
                                                size=len(time_vector))
        time_vector = time_vector + sample_perturbations
        return np.sort(time_vector)

    def _select_random_indices(self, time_vector, keep_percentage):
        """
        Internal functions to randomly select timestamps

        Parameters
        ----------
        time_vector: numpy array
            timestamp vector

        keep_percentage: float/int
            percentage of points retained

        Returns
        -------
        numpy array
            Irregularly sampled timestamps

        """
        num_points = len(time_vector)
        num_select_points = int(keep_percentage*num_points/100)
        index = np.sort(np.random.choice(num_points, size=num_select_points,
                        replace=False))
        return time_vector[index]
