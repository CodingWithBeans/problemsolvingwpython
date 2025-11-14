import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('kpindex.csv')
df = pd.DataFrame(data)
print(data.count()) #271016
print(len(data)) #271016
print(data.max("columns" == "KP"))
print("---" * 20)
plottingdata = df["KP"]

print(data.describe(), plottingdata.describe())

#need to go nd add titles etc but basic set up is there
count, bins, patches = plt.hist(plottingdata, bins=28)
colormap = plt.get_cmap('rainbow', len(patches))

for i, patch in enumerate(patches):
    patch.set_facecolor(colormap(i))
#plt.show()

years = np.arange(1970, 2025)
print(years)
#year_data = data[data['Year'] == year]
# Assume that the variables data and years are already set

# ADD CODE BELOW to initialise a list max_kps 
max_kps = []

# Loop over each year in years
for y in years:

    # ADD CODE BELOW to get the data for year y
    year_data = data[data['Year'] == y]
    # and add the max KP for y to max_kps
    print(type(year_data), year_data)
    yearmax = year_data['KP'].max()
    print(yearmax)
    