# Matplotlib
#
# Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module, which provides a plotting system similar to that of MATLAB.
#
#
# Plotting
#
# The most important function in matplotlib is plot, which allows you to plot 2D data. Here is a simple example:

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# plot the points using matplotlib
plt.plot(x,y)
plt.show() # You must call plt.show() to make graphics appear