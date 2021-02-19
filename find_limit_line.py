#!/usr/bin/env python3
"""
@author: gpwolfe

The third value in popt (corresponding to 'c' in the
function fed to curve_fit) is the upper asympototic limit.

c-a ('a' being the first value in popt) gives the y-intercept,
which is close to 0 in most cases in these experiments.

'b', the second value in popt, defines the rate of decay of the
subtracted term 'a'. At first, 'a' is about as large as 'c', but as the
'x' term grows larger, the function subtracts less and less from 'c',
with 'b' defining this interaction.

If curve_fit cannot fit the data, check to see if the value at 0 is present,
and whether that value is inappropriately high.
"""
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c):
    """Function for limit line."""
    return c-(a * np.exp(-b*x))


def plotty(x_data, y_data, point_name):
    """
    Plot peak intensity versus millisecond value of NMR data.

    Takes a two arrays, one corresponding to delay in milliseconds, the other
    corresponding to the measured peak intensity. Produces a graph with the
    data points, a line of best fit, the upper limit, and the B value, which
    corresponds to the rate of deceleration of the rate of increase (that is,
    how quickly the line of fit bends to horizontal).

    Graph saves as a .png image using string passed as point_name as file name.

    Parameters
    ----------
    x_data : array
        Array or list with millisecond values for x axis.
    y_data : array
        Array or list of peak intensity values.
    point_name : string
        Name used for output file and plot title.

    Returns
    -------
    None.

    """
    popt, pcov = curve_fit(func, x_data, y_data,
                           p0=[max(y_data), .02, max(y_data)])

    # Points for line of fit
    line_x = np.linspace(0, max(x_data))
    line_y = [func(j, *popt) for j in line_x]

    # Plotting experimental data
    plt.scatter(x_data, y_data, marker='o', color='xkcd:royal blue')
    # Plotting line of fit
    plt.plot(line_x, line_y, color='xkcd:deep blue')
    # Plotting line of upper limit
    plt.plot(line_x, [popt[2] for i in line_x], color='xkcd:light blue',
             alpha=.5)
    plt.title(point_name)
    plt.xlabel('delay (milliseconds')
    plt.ylabel('intensity')
    plt.text(x=0, y=popt[2], s="{:.4f}".format(popt[2]))
    plt.text(x=10, y=0, s="y-intercept: {:.4f}".format(popt[0]-popt[2]))
    plt.text(max(x_data), 0, horizontalalignment='right',
             s="C - A * exp(-{:.4f} * x)".format(popt[1]), weight='bold')
    plt.savefig(point_name + '.png')

    plt.clf()
