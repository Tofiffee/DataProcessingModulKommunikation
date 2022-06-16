import pandas as pd
import numpy as np

from Plotting import ScatterPlotSilibleTime


class ChirpData():
    def __init__(self, BaseURL, sheetID):
        self.Basedata = self.ReadBaseData(BaseURL)
        self.sheetID = sheetID

        self.Chirp1 = self.ReadChirpData(self.sheetID, 'Chirp1')
        self.Chirp2 = self.ReadChirpData(self.sheetID, 'Chirp2')
        self.Chirp3 = self.ReadChirpData(self.sheetID, 'Chirp3')
        self.Chirp4 = self.ReadChirpData(self.sheetID, 'Chirp4')
        self.Chirp5 = self.ReadChirpData(self.sheetID, 'Chirp5')

        self.temperature = self.Basedata['temperature'].dropna().iloc[0]
        
        self.syllable1 = self.CalcChirpComponentTime('time_puls1')
        self.syllable2 = self.CalcChirpComponentTime('time_puls2')
        self.syllable3 = self.CalcChirpComponentTime('time_puls3')
        self.syllable4 = self.CalcChirpComponentTime('time_puls4')
        
        self.interTime1 = self.CalcChirpComponentTime('Ruheintervall1')
        self.interTime2 = self.CalcChirpComponentTime('Ruheintervall2')
        self.interTime3 = self.CalcChirpComponentTime('Ruheintervall3')
        
        self.Frequency1 = self.CalcFrequency(1)
        self.Frequency2 = self.CalcFrequency(2)
        self.Frequency3 = self.CalcFrequency(3)
        self.Frequency4 = self.CalcFrequency(4)
        
        self.Chirptimes = self.syllable1 + self.syllable2 + self.syllable3 + self.syllable4 + self.interTime1 + self.interTime2 + self.interTime3

        self.mean_syllable1 = self.syllable1.mean()
        self.mean_syllable2 = self.syllable2.mean()
        self.mean_syllable3 = self.syllable3.mean()
        self.mean_syllable4 = self.syllable4.mean()

    def ReadBaseData(self, url): 
        """
        This function downloads the data from a GoogleTable sheet with the given link and transformes them into a a csv file
        """
        url_read = url.replace('/edit#gid=', '/export?format=csv&gid=')

        df = pd.read_csv(url_read, on_bad_lines='skip')

        return df

    def ReadChirpData(self, sheetID, sheetName):
        url = f'https://docs.google.com/spreadsheets/d/{sheetID}/gviz/tq?tqx=out:csv&sheet={sheetName}'

        df = pd.read_csv(url, on_bad_lines='skip')

        return df

    def CalcChirpComponentTime(self, columnName):
        df_time1 = self.Chirp1[columnName]
        df_time2 = self.Chirp2[columnName]
        df_time3 = self.Chirp3[columnName]
        df_time4 = self.Chirp4[columnName]
        df_time5 = self.Chirp5[columnName]

        dfs = [df_time1, df_time2, df_time3, df_time4, df_time5]

        timevalues = []
            
        for df in dfs:
            df = df.dropna()
            timevalue = df.iloc[-1]
            timevalues.append(timevalue)
        
        timevalues = np.array(timevalues)

        return timevalues

    def CalcFrequency(self, pulsNumber):
        frequ = self.Basedata[[f'Chirp1_puls{pulsNumber}', f'Chirp2_puls{pulsNumber}', f'Chirp3_puls{pulsNumber}']].iloc[0]
        frequ = frequ.apply(lambda x: int(x.split(',')[0]))
        frequ = frequ.to_numpy()

        return frequ


listURL = [
    'https://docs.google.com/spreadsheets/d/13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO/edit#gid=32900920',
    'https://docs.google.com/spreadsheets/d/11YsRYABukndOhe8loN3_4oKDjRfV6mJo/edit#gid=1173836825',
    ]

listSheetID = [
    '13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc',
    '10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO',
    '11YsRYABukndOhe8loN3_4oKDjRfV6mJo',
    ]

syllable1 = []
syllable2 = []
syllabel3 = []
syllabel4 = []
temps = []

for i, j in zip(listURL, listSheetID):
    ChirpObject = ChirpData(i, j)
    syllable1.append(ChirpObject.mean_syllable1)
    print(ChirpObject.mean_syllable1)
    syllable2.append(ChirpObject.mean_syllable2)
    syllabel3.append(ChirpObject.mean_syllable3)
    syllabel4.append(ChirpObject.mean_syllable4)
    temps.append(ChirpObject.temperature)


print(syllable1)
print(syllabel3)
print(syllable2)

ScatterPlotSilibleTime(
    temps=temps, 
    data1=syllable1, data2=syllable2, data3=syllabel3, data4=syllabel4, 
    plotname='SyllableTime'
    )