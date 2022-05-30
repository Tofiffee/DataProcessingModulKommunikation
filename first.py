import pandas as pd



class ChirpData():
    def __init__(self, BaseDataURL) -> None:
        self.BaseDataURL = BaseDataURL
        self.Basedata = ReadData(BaseDataURL)

        def ReadData(url): 
            """
            This function downloads the data from a GoogleTable sheet with the given link and transformes them into a a csv file
            """
            url_read = url.replace('/edit#gid=', '/export?format=csv&gid=')

            df = pd.read_csv(url_read, on_bad_lines='skip')

            return df




sheet_id = '13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc'
sheet_name = 'Chirp1'

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

df = ChirpData.ReadData(url)
print(df.head(10))

a = ChirpData('https://docs.google.com/spreadsheets/d/13Mmcw54O7G_LruX0nXUkFv-C3Y5NNvO6XzAQnhEzeqc/edit#gid=0')
print(a.Basedata)