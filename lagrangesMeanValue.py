import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#initial graph values
xVals = np.linspace(-1, 2.25, 10000)
yVals = (3*(xVals**4)) - (8*(xVals**3)) + (2*(xVals**2)) + (6*(xVals)) + 2

#setting index values for sliders probs move this to the function
aIndex, bIndex = 0, (len(xVals) -1)

#setting apoints x and y values
aPointxVal, aPointyVal = xVals[aIndex], yVals[aIndex]

#setting bpoint x and y valuues can probs also move this to function tbh
bPointxVal, bPointyVal = xVals[bIndex], yVals[bIndex]

#creating figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 3)
ax.set_ylim(0, 12)
plt.subplots_adjust(bottom=0.25)

#creating curve object
curve, = ax.plot(
    xVals,
    yVals,
    label="Function curve",
    color="#000000"
    )

#creating apoint object
apoint, = ax.plot(
    aPointxVal,
    aPointyVal,
    'o',
    label='Point A',
    color="#ff0000"
    )

#creating bpoint object
bpoint, = ax.plot(
    bPointxVal,
    bPointyVal,
    'o',
    label='Point B',
    color="#8800ff"
    )

#creating a line from points a to b
abLinearLine, = ax.plot(
    [aPointxVal, bPointxVal],
    [aPointyVal, bPointyVal],
    color="green",
    linestyle="--",
    label="Linear AB Line"
)

print(dir(curve))
print(curve)
x = curve.get_xdata()
y = curve.get_ydata()
grad = np.gradient(y, x)
print(grad, type(grad))

#setting labels etc
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lagranges Mean Value')
ax.grid(True)
ax.legend()



def createSlider(gridY, name, index, colour):
    """creating sliders\n
    ************************************ \n
    variables:\n
        gridY : float value -> for bottom passed into plt.axis-> 4-tuple of floats rect = (left, bottom, width, height)\n
        name : string value -> naming point on the legend\n
        index : int values -> value of the slider given as a index of the list of xVals, yVals\n
        colour : string value -> pass hex value for colour of the point\n
    ************************************ \n
    Function creates the grid object for the sldier to live in, it then creates a slider for the point A or B setting value max as the length of xvals - 1 \n
    Function returns pointSlider Object"""
    sliderGrid = plt.axes([0.15, gridY, 0.7, 0.03])

    pointSlider = Slider(
    sliderGrid,
    name,
    valmin=0,
    valmax=len(xVals)-1,
    valinit=index,
    valstep=1,
    color=colour
    )

    pointSlider.valtext.set_visible(False)

    return pointSlider

def getGradOfAB():
    "retuns the gradient of straight line between a and b using y2-y1/x2-x1"
    return (bPointyVal - aPointyVal) / (bPointxVal - aPointxVal)

def updateLinearAB():
    
    abLinearLine.set_data(
        [apoint.get_xdata()[0], bpoint.get_xdata()[0]],
        [apoint.get_ydata()[0], bpoint.get_ydata()[0]]
    )
    fig.canvas.draw_idle()

def updateASlider(val):

    index = int(aPointSlider.val)
    aPointxVal = xVals[index]
    aPointyVal = yVals[index]
    apoint.set_data([aPointxVal], [aPointyVal])
    updateLinearAB()

def updateBSlider(val):

    index = int(bPointSlider.val)
    bPointxVal = xVals[index]
    bPointyVal = yVals[index]
    bpoint.set_data([bPointxVal], [bPointyVal])
    updateLinearAB()

# print(getGradOfAB(), type(getGradOfAB()))  ->> 0.734375 <class 'numpy.float64'>
aPointSlider, bPointSlider = createSlider(0.1, "Point A", aIndex, "#ff0000"), createSlider(0.05, "Point B", bIndex, "#8800ff")

aPointSlider.on_changed(updateASlider)
bPointSlider.on_changed(updateBSlider)
for grads in grad:
    if grads == getGradOfAB():
        plt.plot(grad)

plt.show()
