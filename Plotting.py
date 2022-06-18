import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy.stats as stats

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

    result1 = stats.linregress(temps, data1, alternative='greater')
    result2 = stats.linregress(temps, data2, alternative='greater')
    result3 = stats.linregress(temps, data3, alternative='greater')
    result4 = stats.linregress(temps, data4, alternative='greater')

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

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='k', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='k')
    ax0.annotate(f'$R^2$ = {round(result1.rvalue, 2)}\np-value = {round(result1.pvalue,3)}', xy=(21, 0.023), fontsize=20)

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='dimgray', label='syllable 2')
    ax1.plot([max(temps), min(temps)], regression2, color='dimgray')
    ax1.annotate(f'$R^2$ = {round(result2.rvalue, 2)}\np-value = {round(result2.pvalue,3)}', xy=(21, 0.023), fontsize=20)

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='slategrey', label='syllable 3')
    ax2.plot([max(temps), min(temps)], regression3, color='slategrey')
    ax2.annotate(f'$R^2$ = {round(result3.rvalue, 2)}\np-value = {round(result3.pvalue,3)}', xy=(21, 0.023), fontsize=20)

    ax3.errorbar(temps, data4, yerr=yerr4, linestyle='none', marker='o', color='midnightblue', label='syllable 4')
    ax3.plot([max(temps), min(temps)], regression4, color='midnightblue')
    ax3.annotate(f'$R^2$ = {round(result4.rvalue, 2)}\np-value = {round(result4.pvalue,3)}', xy=(21, 0.023), fontsize=20)

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=20, labelpad=10)
        ax.set_ylabel('syllable duration [s]', fontsize=20, labelpad=10)
        ax.set_ylim(0.00, 0.03)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1, fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)

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

    result1 = stats.linregress(temps, data1)
    result2 = stats.linregress(temps, data2)
    result3 = stats.linregress(temps, data3)
    result4 = stats.linregress(temps, data4)

    fig0 = plt.figure(figsize=(15, 15))
    ax0 = plt.subplot(2, 2, 1)
    ax1 = plt.subplot(2, 2, 2)
    ax2 = plt.subplot(2, 2, 3)
    ax3 = plt.subplot(2, 2, 4)
    axs = [ax0, ax1, ax2, ax3]

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='k', label='syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='k')
    ax0.annotate(f'$R^2$ = {round(result1.rvalue,2)}\np-value = {round(result1.pvalue,3)}', xy=(21, 5400), fontsize=18)

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='dimgray', label='syllable 2')
    ax1.plot([max(temps), min(temps)], regression2, color='dimgray')
    ax1.annotate(f'$R^2$ = {round(result2.rvalue,2)}\np-value = {round(result2.pvalue,3)}', xy=(21, 5400), fontsize=18)

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='slategrey', label='syllable 3')
    ax2.plot([max(temps), min(temps)], regression3, color='slategrey')
    ax2.annotate(f'$R^2$ = {round(result3.rvalue,2)}\np-value = {round(result3.pvalue,3)}', xy=(21, 5400), fontsize=18)

    ax3.errorbar(temps, data4, yerr=yerr4, linestyle='none', marker='o', color='midnightblue', label='syllable 4')
    ax3.plot([max(temps), min(temps)], regression4, color='midnightblue')
    ax3.annotate(f'$R^2$ = {round(result4.rvalue,2)}\np-value = {round(result4.pvalue,3)}', xy=(21, 5400), fontsize=18)

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=20, labelpad=10)
        ax.set_ylabel('frequency [Hz]', fontsize=20, labelpad=10)
        ax.set_ylim(3000, 6000)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1, fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)

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

    result1 = stats.linregress(temps, data1, alternative='less')
    result2 = stats.linregress(temps, data2, alternative='less')
    result3 = stats.linregress(temps, data3, alternative='less')

    regression1 = model1.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression2 = model2.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression3 = model3.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))

    fig0 = plt.figure(figsize=(30, 10))
    ax0 = plt.subplot(1, 3, 1)
    ax1 = plt.subplot(1, 3, 2)
    ax2 = plt.subplot(1, 3, 3)
    axs = [ax0, ax1, ax2]

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='k', label='inter syllable 1')
    ax0.plot([max(temps), min(temps)], regression1, color='k')
    ax0.annotate(f'$R^2$ = {round(result1.rvalue,2)}\np-value = {round(result1.pvalue,3)}', xy=(21, 0.026), fontsize=18)

    ax1.errorbar(temps, data2, yerr=yerr2, linestyle='none', marker='o', color='dimgray', label='inter syllable time 2')
    ax1.plot([max(temps), min(temps)], regression2, color='dimgray')
    ax1.annotate(f'$R^2$ = {round(result2.rvalue,2)}\np-value = {round(result2.pvalue,4)}', xy=(21, 0.026), fontsize=18)

    ax2.errorbar(temps, data3, yerr=yerr3, linestyle='none', marker='o', color='slategrey', label='inter syllable time 3')
    ax2.plot([max(temps), min(temps)], regression3, color='slategrey')
    ax2.annotate(f'$R^2$ = {round(result3.rvalue,2)}\np-value = {round(result3.pvalue,4)}', xy=(21, 0.026), fontsize=18)

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=20, labelpad=10)
        ax.set_ylabel('inter syllable time [s]', fontsize=20, labelpad=10)
        ax.set_ylim(0, 0.03)
        handles, lables = ax.get_legend_handles_labels()
        handles = [h[0] for h in handles]
        ax.legend(handles, lables, loc='upper left', numpoints=1, fontsize=20)
        ax.tick_params(axis='both', which='major', labelsize=16)

    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')

def ScatterChirpTimes(
    temps, data1, data2, plotname, yerr1
    ):
    sns.set()
    custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
    sns.set_theme(style='ticks', rc=custom_params)

    temps_train = np.array(temps).reshape(-1, 1)
    model1 = LinearRegression()
    model2 = LinearRegression()

    model1.fit(temps_train, data1)
    model2.fit(temps_train, data2)

    result1 = stats.linregress(temps, data1, alternative='greater')
    result2 = stats.linregress(temps, data2, alternative='greater')

    regression1 = model1.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression2 = model2.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))

    fig0 = plt.figure(figsize=(30, 10))
    ax0 = plt.subplot(1, 2, 1)
    ax1 = plt.subplot(1, 2, 2)
    axs = [ax0, ax1]

    ax0.errorbar(x=temps, y=data1, yerr=yerr1, linestyle='none', marker='o', color='k', label='Chirp Duration')
    ax0.plot([max(temps), min(temps)], regression1, color='k')
    ax0.set_ylim(0, 0.2)
    handles, lables = ax0.get_legend_handles_labels()
    handles = [h[0] for h in handles]
    ax0.legend(handles, lables, loc='upper left', numpoints=1, fontsize=20)
    ax0.set_ylabel('Chirp duration [s]', fontsize=20, labelpad=10)
    ax0.annotate(f'$R^2$ = {round(result1.rvalue,2)}\np-value = {round(result1.pvalue,4)}', xy=(21, 0.16), fontsize=18)

    ax1.scatter(temps, data2, color='k', label='Chirp Frequency')
    ax1.plot([max(temps), min(temps)], regression2, color='k')
    ax1.set_ylim(2, 4)
    ax1.legend(loc='upper left', fontsize=20)
    ax1.set_ylabel('Chirp Frequency [Hz]', fontsize=20, labelpad=10)
    ax1.annotate(f'$R^2$ = {round(result2.rvalue,2)}\np-value = {round(result2.pvalue,4)}', xy=(25, 3.85), fontsize=18)

    for ax in axs:
        ax.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
        ax.set_xlabel('temperature [°C]', fontsize=20, labelpad=10)
        ax.tick_params(axis='both', which='major', labelsize=16)
        
    fig0.tight_layout()
    plt.savefig(f'{plotname}.png')

