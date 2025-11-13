import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('kpindex.csv')
df = pd.DataFrame(data)
print(data.count()) #271016
print(len(data)) #271016
print(data.max("columns" == "KP"))
print(data.describe())

plottingdata = df["KP"]
plot = plottingdata.plot.hist()
plt.show()