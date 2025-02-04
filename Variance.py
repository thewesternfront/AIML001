import numpy as np
import matplotlib.pyplot as plt

def variance():
    pass
    #dataset = [1, 8, 24, 6, 9, 3, 5]
    dataset = [1, 4, 5, 4, 8]
    #dataset = [1, 2, 3, 4, 5, 6, 7, 8]
    diff_from_mean = []
    squared_differences = []
    dataset_mean = np.mean(dataset)
    # find the mean
    print(f'The mean of the data set is {dataset_mean}')

    #find the differences from the mean
    for x in dataset:
        diff_from_mean.append(x - dataset_mean)
        squared_differences.append((x - dataset_mean) ** 2)
    print(f'The variance of the data set is {diff_from_mean}')
    print(f'The squared differences of the data set is {squared_differences}')
    print(f'The Average/Mean of the Squared Differences is {np.mean(squared_differences)}')

    # The standard deviation is just the square root of the variance
    print(f'The standard deviation of the data set is {np.sqrt(np.mean(squared_differences))}')

    #Sample Variance vs Population
    print(f'The sample variance of the data set is {np.var(np.sqrt(squared_differences))}')

def std_dev_var():
    incomes = np.random.normal(100.0, 10.0, 100000)

    plt.hist(incomes, 50)
    plt.show()

    print(f'The standard deviation of the data set is {np.std(incomes)}')
    print(f'The sample variance of the data set is {np.var(incomes)}')