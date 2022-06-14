import pandas as pd
import numpy as np

from Plotting import ScatterPlotSilibleTime


class ChirpData():
    def __init__(self, BaseURL, sheetID):
        self.Basedata = self.ReadBaseData(BaseURL)
        self.sheetID = sheetID
        self.sheetName1 = 'Chirp1'
        self.sheetName2 = 'Chirp2'
        self.sheetName3 = 'Chirp3'
        self.Chirp1 = self.ReadChirpData(self.sheetID, self.sheetName1)
        self.Chirp2 = self.ReadChirpData(self.sheetID, self.sheetName2)
        self.Chirp3 = self.ReadChirpData(self.sheetID, self.sheetName3)
        self.temperature = self.Basedata['Temperatur'].dropna().iloc[0]
        self.syllable1 = self.CalcChirpComponentTime('time_puls1')
        self.syllable2 = self.CalcChirpComponentTime('time_puls2')
        self.syllable3 = self.CalcChirpComponentTime('time_puls3')
        self.syllable4 = self.CalcChirpComponentTime('time_puls4')
        self.interTime1 = self.CalcChirpComponentTime('Ruheintervall1')
        self.interTime2 = self.CalcChirpComponentTime('Ruheintervall2')
        self.interTime3 = self.CalcChirpComponentTime('Ruheintervall3')
        self.refraektaertime = self.CalcChirpComponentTime('Refraektaerzeit')
        self.Frequency1 = self.CalcFrequency(1)
        self.Frequency2 = self.CalcFrequency(2)
        self.Frequency3 = self.CalcFrequency(3)
        self.Frequency4 = self.CalcFrequency(4)
        self.Chirptimes = self.syllable1 + self.syllable2 + self.syllable3 + self.syllable4 + self.interTime1 + self.interTime2 + self.interTime3

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

        dfs = [df_time1, df_time2, df_time3]

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
    ]

listSheetID = [
    '13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc',
    ]

ChirpObjectList = []

for i, j in zip(listURL, listSheetID):
    ChirpObject = ChirpData(i, j)
    ChirpObjectList.append(ChirpObject)

print(ChirpObjectList[0].syllable1)
print(ChirpObjectList[0].interTime1)
print(ChirpObjectList[0].refraektaertime)
print(ChirpObjectList[0].Basedata)
print(ChirpObjectList[0].Frequency3)
print(ChirpObjectList[0].Chirptimes)
# temps = []
# silb1 = []
# silb2 = []
# silb3 = []
# silb4 = []

# for i in ChirpObjectList:
#     silbList = i.CalcSyllableTime()
#     silb1.append(silbList[0])
#     silb2.append(silbList[1])
#     silb3.append(silbList[2])
#     silb4.append(silbList[3])
#     temps.append(i.temperature)

# print(temps)
# print(silb1)
# print(silb2)
# print(silb3)
# print(silb4)

# ScatterPlotSilibleTime(temps, silb1, silb2, silb3, silb4)