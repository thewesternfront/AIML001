from sklearn import datasets
import MachineLearningPipeline as mlp
import Variance as var
from MachineLearningPipeline import *
import PercentilesMoments as pm
import Plots as pl
import CovarianceCorrelation as cc


def main():
    """
    print('in the main method')
    # loading the house prices dataset
    wine_prices = datasets.load_wine()
    print(wine_prices)

    # digits = datasets.load_digits()
    # print(digits.images[4])
    mlp.setup_pipeline()
    """

    # Jupiter Notebook Course
    # mlp.jupyternotebook()
    # var.variance()
    cc.covariance_correlation()
    # var.std_dev_var()
    # pm.perc_mom()
    # pm.moments()
    # pl.plotting()
    # pl.scatterplot()
    ###pl.seaborn()


if __name__ == '__main__':
    main()



