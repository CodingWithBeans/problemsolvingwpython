import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def creatingVariables():
    #creating variables to be used later in the script
    data = pd.read_csv('kpindex.csv')


    plottingdata = data["KP"]

    years = np.arange(1970, 2025)
    return data, plottingdata, years

def printstatements(plottingdata, data):
    #some simple print statements for the first few questions
    print(data.describe(), plottingdata.describe())
    print(data.count()) #271016
    print(len(data)) #271016
    print(data.max("columns" == "KP"))
    print("---" * 20)

def firstGraph(plottingdata):

    #creating the plot
    plt.hist(plottingdata, bins=28, density=True, edgecolor="black")

    #tried to add distribution curve, it looks nasty
    #plottingdata.plot(kind='density', linewidth=2)

    #labels etc
    plt.title("Distribution of KP Index Values")
    plt.xlabel("KP Value")
    plt.ylabel("Density")
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
    #line graph of kp index max per year

    #creating plot
    plt.plot(years, max_kps)

    #graph GUI output stuff
    plt.title("Maximum Kp Index per Year")
    plt.xlabel("Year")
    plt.ylabel("Maximum Kp Value recorded within the year")
    plt.show()

def significantYears(data):
    #create significant years set, using set/list comprehension adding year to the set loops from the lowest year in the data to the max year + 1 as 0 based index
    # if we find any year with a kps value == to the maximum permitted kpvalue then add to the set
    significant_years = {year for year in range(data['Year'].min(), data['Year'].max() + 1) if any(data.loc[data['Year'] == year, 'KP'] == data['KP'].max())}
    return significant_years

def createSingleDaybar(date, data):

    #data stream
    day_data = data[(data['Year']==date[0]) &
                    (data['Month']==date[1]) &
                    (data['Day']==date[2])]

    kps = day_data["KP"]
    hours = day_data["Period_Start"]
    indexvcolours = {1:"#000000",2:"#f700ff", 3:"#6200ff", 4:"#0004ff", 5:"#00d9ff", 6:"#00ff00", 7:"#fffb00", 8:"#ff6600", 9:"#ff0000",}
    
    #initialise bar chart

    #here i initialise the bar chart with hours on the x axis, kps on the y axis, i aligned each chart in the center. for the colours i have set the rounded value of the kp for the time period using the dictionary indexvcolours as a colour map, edge colour and linewidth are to seperate each bar for visual reading
    plt.bar(hours, kps, width=3, align='center', color = [indexvcolours[round(kp)] for kp in kps], edgecolor="white", linewidth=0.5)

    #titles takes the date variable, converts to a string and slices the [] from the front and back
    plt.title(f"The Kp Index on {str(date)[1:-1]}")


    #X- axis
    plt.xlabel("Hour")
    
    #set the limit to go between -2 and 24, set the ticks of the graph to be = to 3
    plt.xticks(range(0, 25, 3))
    plt.xlim(-2,24)

    #Y - axis
    plt.yticks(range(0, 10))
    plt.ylim(0, max(kps) + 1)
    plt.ylabel("KP")
    plt.show()

def main():
    #main script

    #create variables
    data, plottingdata, years = creatingVariables()

    #creating maxkps
    max_kps = maxkpsCreation(data, years)

    #printing statements for questions / debugging
    printstatements(plottingdata, data)

    #histogram graph
    firstGraph(plottingdata)

    #line graph
    secondGraph(max_kps, years)

    #siginificant years creation
    significantYears(data)

    #dates to make bar charts out
    dates = [[1972,8,5], [2024,5,11]]

    #for loop to make 2 bar charts
    for date in dates:
        createSingleDaybar(date, data)
    


if __name__ == "__main__":
    main()

