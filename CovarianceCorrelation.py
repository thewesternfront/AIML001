import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import pandas as pd
from pylab import *



def de_mean(x):
    xmean = mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)

def covariance_correlation():
    pageSpeeds = np.random.normal(3.0, 1.0, 1000)
    purchaseAmount = np.random.normal(50.0, 10.0, 1000)
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    print(covariance(pageSpeeds, purchaseAmount))
