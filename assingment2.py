import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def creatingVariables():
    data = pd.read_csv('kpindex.csv')
    df = pd.DataFrame(data)

    plottingdata = df["KP"]

    years = np.arange(1970, 2025)
    return data, plottingdata, years

def printstatements(plottingdata, data):

    print(data.describe(), plottingdata.describe())
    print(data.count()) #271016
    print(len(data)) #271016
    print(data.max("columns" == "KP"))
    print("---" * 20)

def firstGraph(plottingdata):
    #need to go nd add titles etc but basic set up is there
    count, bins, patches = plt.hist(plottingdata, bins=28)
    colormap = plt.get_cmap('rainbow', len(patches))

    for i, patch in enumerate(patches):
        patch.set_facecolor(colormap(i))
    plt.show()


def maxkpsCreation(data, years):
    # ADD CODE BELOW to initialise a list max_kps 
    max_kps = []

    # Loop over each year in years
    for y in years:

        # ADD CODE BELOW to get the data for year y
        year_data = data[data['Year'] == y]
        # and add the max KP for y to max_kps
        max_kps.append(year_data['KP'].max())
    return max_kps

def secondGraph(max_kps, years):
    #// line graph of years vs max kps go put titles and stuff on this matty haway
    plt.plot(years, max_kps)
    plt.show()

def significantYears(data):

    significant_years = {year for year in range(data['Year'].min(), data['Year'].max() + 1) if any(data.loc[data['Year'] == year, 'KP'] == data['KP'].max())}
    print(significant_years, type(significant_years))
    return significant_years

def createSingleDayHisto(date, data): 
    # Get rows for this day
    day_data = data[(data['Year']==date[0]) &
                    (data['Month']==date[1]) &
                    (data['Day']==date[2])]
    print(day_data)
    kps = day_data["KP"]
    hours = day_data["Period_Start"]
    indexvcolours = {1:"#ff0000", 2:"#3cff00", 3:"#e100ff", 4:"#eeff00", 5:"#0044ff", 6:"#00e1ff", 7:"#ff5100", 0:"#ff009d",}
    

    print(hours, "hours", "-" * 20)
    print(kps, "kps", "-" * 20)
    plt.bar(hours, kps, width=3, align='edge', color = [indexvcolours[] for kp in kps])
    plt.show()
    plt.bar(hours, kps, width=3, align="center")
    plt.show()

def main():
    data, plottingdata, years = creatingVariables()
    max_kps = maxkpsCreation(data, years)
    printstatements(plottingdata, data)
    firstGraph(plottingdata)
    secondGraph(max_kps, years)
    significantYears(data)
    dates = [[1972,8,5], [2024,5,11]]
    for date in dates:
        createSingleDayHisto(date, data)
    


if __name__ == "__main__":
    main()

