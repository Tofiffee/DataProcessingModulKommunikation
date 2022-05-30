import pandas as pd
import numpy as np


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

    def CalcChirpTime(self):
        df_time1 = self.Chirp1[['time_puls1', 'time_puls2', 'time_puls3', 'time_puls4']]
        df_time2 = self.Chirp2[['time_puls1', 'time_puls2', 'time_puls3', 'time_puls4']]
        df_time3 = self.Chirp3[['time_puls1', 'time_puls2', 'time_puls3', 'time_puls4']]

        index = ['time_puls1', 'time_puls2', 'time_puls3', 'time_puls4']
        dfs = [df_time1, df_time2, df_time3]

        for i in index:
            timevalues = []
            for df in dfs:
                time_df = df[i].dropna()
                timevalue = time_df.iloc[-1]
                timevalues.append(timevalue)
            
            timevalues = np.array(timevalues)
            meanvalue = timevalues.mean()
            print(meanvalue)


listURL = [
    'https://docs.google.com/spreadsheets/d/13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/1fxWvhPUXpSmtIRLDqH69WiPEx0G7_hj02Oxop-hmeNY/edit#gid=0',
    'https://docs.google.com/spreadsheets/d/10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO/edit#gid=32900920',
    'https://docs.google.com/spreadsheets/d/11YsRYABukndOhe8loN3_4oKDjRfV6mJo/edit#gid=1173836825',
    'https://docs.google.com/spreadsheets/d/1iDDoF2KZkfagIcAxF7ymU1Q2ClAGGkNW/edit#gid=1498647522'
    ]

listSheetID = [
    '13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc',
    '1fxWvhPUXpSmtIRLDqH69WiPEx0G7_hj02Oxop-hmeNY',
    '10qs8ioTX_lJuN4jY4pEuxdkQ2LTC84cO',
    '11YsRYABukndOhe8loN3_4oKDjRfV6mJo',
    '1iDDoF2KZkfagIcAxF7ymU1Q2ClAGGkNW'
    ]

ChirpObjectList = []

for i, j in zip(listURL, listSheetID):
    ChirpObject = ChirpData(i, j)
    ChirpObjectList.append(ChirpObject)

for i in ChirpObjectList:
    i.CalcChirpTime()