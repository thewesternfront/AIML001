import matplotlib
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt

def setup_pipeline():
    pass

def jupyternotebook():
    #%matplotlibinline
    import numpy as np
    import matplotlib.pyplot as plt

    incomes = np.random.normal(27000, 15000, 10000)
    #incomes = np.append(incomes, [1000000000])

    plt.hist(incomes, 50)
    plt.show()

    print(incomes.mean())

    u = np.median(incomes)
    s = np.std(incomes)
    filtered = [e for e in incomes if (u - 2 * s < e < u + 2 * s)]
    return filtered

    filtered = reject_outliers(incomes)

    plt.hist(filtered, 50)
    plt.show()

