import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def ScatterPlotSilibleTime(
    temps, data1, data2, data3, data4, plotname,
    yerr1, yerr2, yerr3, yerr4
    ):
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

    r2_1 = r2_score(data1, model1.predict(temps_train))

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

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='blue', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='blue')
    ax0.annotate(f'{r2_1}', )

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='red', label='syllable 2')
    ax1.plot([max(temps), min(temps)], regression2, color='red')

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='green', label='syllable 3')
    ax2.plot([max(temps), min(temps)], regression3, color='green')

    ax3.errorbar(temps, data4, yerr=yerr4, linestyle='none', marker='o', color='k', label='syllable 4')
    ax3.plot([max(temps), min(temps)], regression4, color='k')

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=16, labelpad=10)
        ax.set_ylabel('syllable duration [s]', fontsize=16, labelpad=10)
        ax.set_ylim(0.00, 0.03)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1)

    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')

def ScatterPlotFrequency(
    temps, data1, data2, data3, data4, plotname,
    yerr1, yerr2, yerr3, yerr4
    ):
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

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='blue', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='blue')

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='red', label='syllable 1')
    ax1.plot([max(temps), min(temps)], regression2, color='red')

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='green', label='syllable 1')
    ax2.plot([max(temps), min(temps)], regression3, color='green')

    ax3.errorbar(temps, data4, yerr=yerr4, linestyle='none', marker='o', color='k', label='syllable 1')
    ax3.plot([max(temps), min(temps)], regression4, color='k')

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=16, labelpad=10)
        ax.set_ylabel('frequency [Hz]', fontsize=16, labelpad=10)
        ax.set_ylim(3000, 6000)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1)

    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')

def ScatterPlotInterTime(
    temps, data1, data2, data3, plotname,
    yerr1, yerr2, yerr3
    ):
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    temps_train = np.array(temps).reshape(-1, 1)
    model1 = LinearRegression()
    model2 = LinearRegression()
    model3 = LinearRegression()

    model1.fit(temps_train, data1)
    model2.fit(temps_train, data2)
    model3.fit(temps_train, data3)

    regression1 = model1.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression2 = model2.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression3 = model3.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))

    fig0 = plt.figure(figsize=(15, 15))
    ax0 = plt.subplot(1, 3, 1)
    ax1 = plt.subplot(1, 3, 2)
    ax2 = plt.subplot(1, 3, 3)
    axs = [ax0, ax1, ax2]

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='blue', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='blue')

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='red', label='syllable 1')
    ax1.plot([max(temps), min(temps)], regression2, color='red')

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='green', label='syllable 1')
    ax2.plot([max(temps), min(temps)], regression3, color='green')

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=16, labelpad=10)
        ax.set_ylabel('frequency [Hz]', fontsize=16, labelpad=10)
        ax.set_ylim(3000, 6000)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1)

    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')
