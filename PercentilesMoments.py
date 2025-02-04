import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp


def perc_mom():
    center = 0
    stdev = 2
    num_data_points = 100000
    vals = np.random.normal(center, stdev, num_data_points)
    print(f'data centered around {center}, with a standard deviation of {stdev} and {num_data_points} data points')

    plt.hist(vals, 100)
    plt.show()

    percentile = np.percentile(vals, 50)
    print(f'The fifty percentile (median) is {percentile}')
    percentile = np.percentile(vals, 90)
    print(f'The ninety percentile () is {percentile}')
    percentile = np.percentile(vals, 20)
    print(f'The twenty percentile () is {percentile}')


def moments():
    # moment 1 - mean
    # moment 2 - variance
    # moment 3 - skew
    # moment 4 - kurtosis
    # MOMENTS deal with the shape of the data

    vals = np.random.normal(10, 0.5, 10000)

    plt.hist(vals, 50)
    plt.show()

    print(f'the first MOMENT is the mean - {np.mean(vals)}')
    print(f'The second MOMENT is the variance - {np.std(vals)}')
    print(f'The third MOMENT is the skew - {sp.skew(vals)}')
    print(f'The fourth MOMENT is the kurtosis - {sp.kurtosis(vals)}')
