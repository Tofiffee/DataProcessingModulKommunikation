from ChirpDataClass import ChirpData
<<<<<<< HEAD
from Plotting import ScatterPlotFrequency, ScatterPlotInterTime, ScatterPlotSilibleTime, ScatterChirpTimes
from statisticsPipline import StatisticalTesting
=======
from Plotting import ScatterPlotFrequency, ScatterPlotSilibleTime
from normalDistribution import TestNormalDistribution
>>>>>>> main


listURL = [
    'https://docs.google.com/spreadsheets/d/13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO/edit#gid=32900920',
    'https://docs.google.com/spreadsheets/d/11YsRYABukndOhe8loN3_4oKDjRfV6mJo/edit#gid=1173836825',
    'https://docs.google.com/spreadsheets/d/1JJEj3W6ArKlXMpKFDegExBoJWBMxIh3mMfZK_CSEdR4/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1xL9Nz2XXg6fb7bUjv4_2_Meu2xLrXBlmTF_4sCoXvnA/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/10Rh9E4rtgbJqGvTNuXByqJi1wz41gqdZLwluavlvpu4/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1UCJaaM2F_uuebvnyMMxybjBbQ3c4rN79CTmuOT2A9Pg/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1XohcjrEkX4A9Fdf_jNLRN00v2IZjTEUW6dfQV4M6iaA/edit#gid=0'
    ]

listSheetID = [
    '13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc',
    '10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO',
    '11YsRYABukndOhe8loN3_4oKDjRfV6mJo',
    '1JJEj3W6ArKlXMpKFDegExBoJWBMxIh3mMfZK_CSEdR4',
    '1xL9Nz2XXg6fb7bUjv4_2_Meu2xLrXBlmTF_4sCoXvnA',
    '10Rh9E4rtgbJqGvTNuXByqJi1wz41gqdZLwluavlvpu4',
    '1UCJaaM2F_uuebvnyMMxybjBbQ3c4rN79CTmuOT2A9Pg',
    '1XohcjrEkX4A9Fdf_jNLRN00v2IZjTEUW6dfQV4M6iaA'
    ]


syllable1 = []
syllbErr1 = []
syllable2 = []
syllbErr2 = []
syllabel3 = []
syllbErr3 = []
syllabel4 = []
syllbErr4 = []

Frequ1 = []
FrequErr1 = []
Frequ2 = []
FrequErr2 = []
Frequ3 = []
FrequErr3 = []
Frequ4 = []
FrequErr4 = []

interTime1 = []
interTimeErr1 = []
interTime2 = []
interTimeErr2 = []
interTime3 = []
interTimeErr3 = []

echemeTime = []
echemeTimeErr = []
Chirpfrequ = []


temps = []
counter = 0

for i, j in zip(listURL, listSheetID):
    ChirpObject = ChirpData(i, j)
<<<<<<< HEAD
=======
    counter += 1
    print(counter)
    print(TestNormalDistribution(ChirpObject.syllable1, 'syllable1'))
    print(TestNormalDistribution(ChirpObject.syllable2, 'syllable2'))
    print(TestNormalDistribution(ChirpObject.syllable3, 'syllable3'))
    print(TestNormalDistribution(ChirpObject.syllable4, 'syllable4'))

    print(TestNormalDistribution(ChirpObject.interTime1, 'interTime1'))
    print(TestNormalDistribution(ChirpObject.interTime2, 'interTime2'))
    print(TestNormalDistribution(ChirpObject.interTime3, 'interTime3'))

    print(TestNormalDistribution(ChirpObject.Frequency1, 'Frequency1'))
    print(TestNormalDistribution(ChirpObject.Frequency2, 'Frequency2'))
    print(TestNormalDistribution(ChirpObject.Frequency3, 'Frequency3'))
    print(TestNormalDistribution(ChirpObject.Frequency4, 'Frequency4'))
>>>>>>> main

    syllable1.append(ChirpObject.mean_syllable1)
    syllable2.append(ChirpObject.mean_syllable2)
    syllabel3.append(ChirpObject.mean_syllable3)
    syllabel4.append(ChirpObject.mean_syllable4)
    
    syllbErr1.append(ChirpObject.std_syllable1)
    syllbErr2.append(ChirpObject.std_syllable2)
    syllbErr3.append(ChirpObject.std_syllable3)
    syllbErr4.append(ChirpObject.std_syllable4)

    Frequ1.append(ChirpObject.meanFrequency1)
    Frequ2.append(ChirpObject.meanFrequency2)
    Frequ3.append(ChirpObject.meanFrequency3)
    Frequ4.append(ChirpObject.meanFrequency4)

    FrequErr1.append(ChirpObject.stdFrequency1)
    FrequErr2.append(ChirpObject.stdFrequency2)
    FrequErr3.append(ChirpObject.stdFrequency3)
    FrequErr4.append(ChirpObject.stdFrequency4)

    interTime1.append(ChirpObject.meanInterTime1)
    interTime2.append(ChirpObject.meanInterTime2)
    interTime3.append(ChirpObject.meanInterTime3)

    interTimeErr1.append(ChirpObject.stdInterTime1)
    interTimeErr2.append(ChirpObject.stdInterTime2)
    interTimeErr3.append(ChirpObject.stdInterTime3)

    echemeTime.append(ChirpObject.meanChirptime)
    echemeTimeErr.append(ChirpObject.stdChirptime)
    Chirpfrequ.append(ChirpObject.ChirpFrequency)

    temps.append(ChirpObject.temperature)

print(Chirpfrequ)

ScatterPlotSilibleTime(
    temps=temps, 
    data1=syllable1, data2=syllable2, data3=syllabel3, data4=syllabel4, 
    plotname='SyllableTime',
    yerr1=syllbErr1, yerr2=syllbErr2, yerr3=syllbErr3, yerr4=syllbErr4
    )

ScatterPlotFrequency(
    temps=temps,
    data1=Frequ1, data2=Frequ2, data3=Frequ3, data4=Frequ4,
    plotname='FrequencyTemp',
    yerr1=FrequErr1, yerr2=FrequErr2, yerr3=FrequErr3, yerr4=FrequErr4
    )

ScatterPlotInterTime(
    temps=temps, data1=interTime1, data2=interTime2, data3=interTime3,
    yerr1=interTimeErr1, yerr2=interTimeErr2, yerr3=interTimeErr3,
    plotname='interTime'
    )

ScatterChirpTimes(
    temps=temps, data1=echemeTime, data2=Chirpfrequ, plotname='Chirptime_frequency', yerr1=echemeTimeErr
    )