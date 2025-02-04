import numpy as np
import matplotlib.pyplot as plt


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
