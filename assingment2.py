import pandas as pd

data = pd.read_csv('kpindex.csv')
print(data.count()) #271016

print(data.max("columns" == "KP"))
print(data.describe())



