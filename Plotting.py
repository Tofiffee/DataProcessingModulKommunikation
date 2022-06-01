import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

sns.set()
custom_params = {'axes.spines.right': False, 'axes.spines.top': False}
sns.set_theme(style='ticks', rc=custom_params)


def ScatterPlotSilibleTime(temps, silb1, silb2, silb3, silb4):
    temps_train = np.array(temps).reshape(-1, 1)
    model1 = LinearRegression()
    model2 = LinearRegression()
    model3 = LinearRegression()
    model4 = LinearRegression()

    model1.fit(temps_train, silb1)
    model2.fit(temps_train, silb2)
    model3.fit(temps_train, silb3)
    model4.fit(temps_train, silb4)

    regression1 = model1.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression2 = model2.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression3 = model3.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))
    regression4 = model4.predict(np.array([max(temps), min(temps)]).reshape(-1, 1))

    fig0, ax0 = plt.subplots(figsize=(15, 10))
    ax0.set_xlim(np.floor(min(temps))-1, np.ceil(max(temps)))
    ax0.set_ylim(0.01, 0.025)


    plt.scatter(temps, silb1, color='blue', label='syllable 1')
    plt.scatter(temps, silb2, color='red', label='syllable 2')
    plt.scatter(temps, silb3, color='green', label='syllable 3')
    plt.scatter(temps, silb4, color='k', label='syllable 4')
    plt.plot([max(temps), min(temps)], regression1, color='blue')
    plt.plot([max(temps), min(temps)], regression2, color='red')
    plt.plot([max(temps), min(temps)], regression3, color='green')
    plt.plot([max(temps), min(temps)], regression4, color='k')

    plt.legend(loc='best')
    plt.savefig('siliblesPlot.png')
