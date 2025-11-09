import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

xVals = np.linspace(-1, 2.25, 10000)
yVals = (3*(xVals**4)) - (8*(xVals**3)) +(2*(xVals**2))+(6*(xVals)) + 2

aIndex, bIndex = 0, (len(xVals) -1)

aPointxVal, aPointyVal = xVals[aIndex], yVals[aIndex]

bPointxVal, bPointyVal = xVals[bIndex], yVals[bIndex]

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 3)
ax.set_ylim(0, 12)
plt.subplots_adjust(bottom=0.25)

curve, = ax.plot(
    xVals,
    yVals,
    label="Function curve",
    color="#000000"
    )

apoint, = ax.plot(
    aPointxVal,
    aPointyVal,
    'o',
    label='Point A',
    color="#ff0000"
    )

bpoint, = ax.plot(
    bPointxVal,
    bPointyVal,
    'o',
    label='Point B',
    color="#8800ff"
    )

abLinearLine, = ax.plot(
    [aPointxVal, bPointxVal],
    [aPointyVal, bPointyVal],
    color="green",
    linestyle="--",
    label="Linear AB Line"
)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lagranges Mean Value')
ax.grid(True)
ax.legend()

slider_ax_a = plt.axes([0.15, 0.1, 0.7, 0.03])
slider_ax_b = plt.axes([0.15, 0.05, 0.7, 0.03])

aPointSlider = Slider(
    slider_ax_a,
    "point A",
    valmin=0,
    valmax=len(xVals)-1,
    valinit=aIndex,
    valstep=1,
    track_color="#ff0000"
    )
aPointSlider.valtext.set_visible(False)


bPointSlider = Slider(
    slider_ax_b,
    "point B",
    valmin=1,
    valmax=len(xVals)-1,
    valinit=bIndex,
    valstep=1,
    initcolor="#8800ff"
    )
bPointSlider.valtext.set_visible(False)

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

aPointSlider.on_changed(updateASlider)
bPointSlider.on_changed(updateBSlider)
plt.show()