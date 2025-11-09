import numpy as np
t = np.linspace(0.3, 8, 500)

x = (1.5 * t) + (np.cos(11 * t) / t)
y = (1.5 * t) + (np.sin(11 * t) / t)

lastx, lasty = x[499], y[499]
firstx, firsty = x[0], y[0]


print(f"first x value = {firstx}, first y value = {firsty}")
print(f"last x = {lastx}, lasty = {lasty}")


q4 = abs(y-x)[499]
print(q4)