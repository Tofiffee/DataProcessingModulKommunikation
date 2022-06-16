import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

def ScatterPlotSilibleTime(temps, data1, data2, data3, data4, plotname):
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    temps_train = np.array(temps).reshape(-1, 1)
    model1 = LinearRegression()
    model2 = LinearRegression()
    model3 = LinearRegression()
    model4 = LinearRegression()

    model1.fit(temps_train, data1)
    model2.fit(temps_train, data2)
    model3.fit(temps_train, data3)
    model4.fit(temps_train, data4)

    regression1 = model1.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression2 = model2.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression3 = model3.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression4 = model4.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))

    fig0 = plt.figure(figsize=(15, 15))
    ax0 = plt.subplot(2, 2, 1)
    ax1 = plt.subplot(2, 2, 2)
    ax2 = plt.subplot(2, 2, 3)
    ax3 = plt.subplot(2, 2, 4)
    axs = [ax0, ax1, ax2, ax3]
    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature', fontsize=16, labelpad=10)
        ax.set_ylabel('silible duration [s]', fontsize=16, labelpad=10)
        ax.set_ylim(0.01, 0.025)
        ax.legend(loc='best')

    ax0.scatter(temps, data1, color='blue', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='blue')

    ax1.scatter(temps, data2, color='red', label='syllable 2')
    ax1.plot([max(temps), min(temps)], regression2, color='red')

    ax2.scatter(temps, data3, color='green', label='syllable 3')
    ax2.plot([max(temps), min(temps)], regression3, color='green')

    ax3.scatter(temps, data4, color='k', label='syllable 4')
    ax3.plot([max(temps), min(temps)], regression4, color='k')

    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')
