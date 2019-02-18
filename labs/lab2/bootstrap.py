import matplotlib

matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np
import numpy.random as npr


def bootstrap(sample, sample_size, iterations):
    # <---INSERT YOUR CODE HERE--->

    arr = np.empty((iterations, 5))

    mean_arr = np.empty(iterations)

    #idx = npr.randint(sample_size, size=5)
    # for a in range(0, iterations):
    # 	for j in range(0, sample_size):
    # 		arr[a][j] = sample[idx[j]]
    # 	mean_arr[a] = np.mean(arr[a])

    for a in range(0, iterations):
        arr[a] = np.random.choice(sample, 5, replace=True)
        print(arr[a])
        mean_arr[a] = np.mean(arr[a])

    data_mean = np.mean(arr)

    lower = 0
    upper = 1

    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')

    data = df.values.T[0]

    data_size = data.shape[0]

    boots = []
    for i in range(100, 10000, 1000):
        boot = bootstrap(data, data_size, i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, 10000)

    sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')

# print ("Mean: %f")%(np.mean(data))
# print ("Var: %f")%(np.var(data))
