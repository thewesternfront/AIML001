import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
from pylab import randn

def plotting():
    """
    x = np.arange(-3, 3, 0.01)

    # plot 1
    plt.plot(x, sp.norm.pdf(x))
    plt.show()

    # plot 2
    plt.plot(x, sp.norm.pdf(x))
    plt.plot(x, sp.norm.pdf(x, 1.0, 0.5))
    plt.show()

    # Save plot to file
    plt.plot(x, sp.norm.pdf(x))
    plt.plot(x, sp.norm.pdf(x, 1.0, 0.5))
    plt.savefig('MyPlot.png', format='png')

    """
    # Plot Multiple Functions
    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-1, 1, 50)
    # calculate the y value for each element of the x vector
    y1 = x ** 1
    y2 = x ** 2
    y3 = x ** 3

    # fig, ax = plt.subplots()
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)

    # ADding to the graph for presentation, labels, grids, etc.
    plt.xlabel('X Value')
    plt.ylabel('f(x)')
    plt.plot(x, y1, 'b+')
    plt.plot(x, y2, 'r_')
    plt.plot(x, y3, 'g^')
    plt.legend(['X^1', 'X^2', 'X^3'], loc=4)
    plt.grid(True)
    plt.show()

def scatterplot():
    #age = [12,14,16,18,20,22,24,26,28,30,31,34,36,38,40,42,44,46,48,50]
    #hop = [1,1,1,2,2,3,4,5,5,5,5,4,4,4,4,3,3,3,2,2]
    age = randn(10, 30, 4)
    hop = randn(10, 30, 4)

    plt.scatter(age, hop)
    plt.legend(['Hours Practiced based on Age'], loc=4)
    plt.xlabel('Age')
    plt.ylabel('Hours Practiced')
    plt.show()

def seaborn():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_style('darkgrid')

    # df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
    df = pd.read_csv("C:\\Users\\cymru.MSI\\Downloads\\TroyFuelEfficiency.csv")

    gear_counts = df['# Gears'].value_counts()
    gear_counts.plot(kind='bar')
    plt.show()

    # Closer look at the data plotted:
    print('DATA:')
    # DF is a DataFrame
    print(df.head())
    print(df.describe())
    # print(df.plot.bar())

    # New Data Frame based on df dlwnloaded from site using CSV data for
    # Fuel Efficiency
    df2 = df[['Cylinders', 'CityMPG', '# Gears']]
    print(df2.head())

    # Seaborn plot comparing # Cylinders to MPG, etc.
    sns.pairplot(df2, hue='Cylinders', height=4.0)
    plt.show()