import pandas as pd

data = pd.read_excel("RfqData.xlsx", sheet_name=1)
data.Traded.replace('MISSED', 0, inplace=True)
data.Traded.replace('DONE', 1, inplace=True)
data.to_csv("test_data.csv", index=False)

b0 = data[data.Bond=='Bond_0']
b1 = data[data.Bond=='Bond_1']
b2 = data[data.Bond=='Bond_2']


