import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    print((df.columns))
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)

    sns_plot.savefig("scaterplot_vehicles.png",bbox_inches='tight')
    sns_plot.savefig("scaterplot_vehicles.pdf",bbox_inches='tight')

    data = df.values.T[0]

    plt.clf()
    sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('MPG')
    axes.set_ylabel('Count')

    sns_plot2.savefig("histogram_vehicles.png", bbox_inches='tight')
    sns_plot2.savefig("histogram_vehicles.pdf", bbox_inches='tight')
