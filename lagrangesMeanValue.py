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

#print(dir(abLinearLine))
#['_PROPERTIES_EXCLUDED_FROM_SET', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_agg_filter', '_alias_map', '_alpha', '_animated', '_antialiased', '_axes', '_callbacks', '_clipon', '_clippath', '_cm_set', '_color', '_dash_pattern', '_dashcapstyle', '_dashjoinstyle', '_different_canvas', '_drawStyles_l', '_drawStyles_s', '_drawstyle', '_fully_clipped_to_axes', '_gapcolor', '_get_markerfacecolor', '_get_transformed_path', '_gid', '_in_layout', '_internal_update', '_invalidx', '_invalidy', '_label', '_lineStyles', '_linestyle', '_linestyles', '_linewidth', '_marker', '_markeredgecolor', '_markeredgewidth', '_markerfacecolor', '_markerfacecoloralt', '_markersize', '_markevery', '_mouseover', '_parent_figure', '_path', '_path_effects', '_picker', '_pickradius', '_rasterized', '_remove_method', '_set_alpha_for_array', '_set_gc_clip', '_set_markercolor', '_sketch', '_snap', '_solidcapstyle', '_solidjoinstyle', '_stale', '_sticky_edges', '_subslice', '_subslice_optim_min_size', '_transform', '_transformSet', '_transform_path', '_transformed_path', '_unscaled_dash_pattern', '_update_props', '_update_set_signature_and_docstring', '_url', '_visible', '_x', '_x_filled', '_xorig', '_xy', '_y', '_yorig', 'add_callback', 'axes', 'clipbox', 'contains', 'convert_xunits', 'convert_yunits', 'draw', 'drawStyleKeys', 'drawStyles', 'figure', 'fillStyles', 'filled_markers', 'findobj', 'format_cursor_data', 'get_aa', 'get_agg_filter', 'get_alpha', 'get_animated', 'get_antialiased', 'get_bbox', 'get_c', 'get_children', 'get_clip_box', 'get_clip_on', 'get_clip_path', 'get_color', 'get_cursor_data', 'get_dash_capstyle', 'get_dash_joinstyle', 'get_data', 'get_drawstyle', 'get_ds', 'get_figure', 'get_fillstyle', 'get_gapcolor', 'get_gid', 'get_in_layout', 'get_label', 'get_linestyle', 'get_linewidth', 'get_ls', 'get_lw', 'get_marker', 'get_markeredgecolor', 'get_markeredgewidth', 'get_markerfacecolor', 'get_markerfacecoloralt', 'get_markersize', 'get_markevery', 'get_mec', 'get_mew', 'get_mfc', 'get_mfcalt', 'get_mouseover', 'get_ms', 'get_path', 'get_path_effects', 'get_picker', 'get_pickradius', 'get_rasterized', 'get_sketch_params', 'get_snap', 'get_solid_capstyle', 'get_solid_joinstyle', 'get_tightbbox', 'get_transform', 'get_transformed_clip_path_and_affine', 'get_url', 'get_visible', 'get_window_extent', 'get_xdata', 'get_xydata', 'get_ydata', 'get_zorder', 'have_units', 'ind_offset', 'is_dashed', 'is_transform_set', 'lineStyles', 'markers', 'mouseover', 'pchanged', 'pick', 'pickable', 'pickradius', 'properties', 'recache', 'recache_always', 'remove', 'remove_callback', 'set', 'set_aa', 'set_agg_filter', 'set_alpha', 'set_animated', 'set_antialiased', 'set_c', 'set_clip_box', 'set_clip_on', 'set_clip_path', 'set_color', 'set_dash_capstyle', 'set_dash_joinstyle', 'set_dashes', 'set_data', 'set_drawstyle', 'set_ds', 'set_figure', 'set_fillstyle', 'set_gapcolor', 'set_gid', 'set_in_layout', 'set_label', 'set_linestyle', 'set_linewidth', 'set_ls', 'set_lw', 'set_marker', 'set_markeredgecolor', 'set_markeredgewidth', 'set_markerfacecolor', 'set_markerfacecoloralt', 'set_markersize', 'set_markevery', 'set_mec', 'set_mew', 'set_mfc', 'set_mfcalt', 'set_mouseover', 'set_ms', 'set_path_effects', 'set_picker', 'set_pickradius', 'set_rasterized', 'set_sketch_params', 'set_snap', 'set_solid_capstyle', 'set_solid_joinstyle', 'set_transform', 'set_url', 'set_visible', 'set_xdata', 'set_ydata', 'set_zorder', 'stale', 'stale_callback', 'sticky_edges', 'update', 'update_from', 'zorder']

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
plt.show()
