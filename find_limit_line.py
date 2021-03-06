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
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_absolute_error, mean_squared_error


def limit_func(x, a, b, c):
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

    Graph saves as a .pdf image using string passed as point_name as file name.

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
    try:
        popt, pcov = curve_fit(limit_func, x_data, y_data,
                               p0=[max(y_data), .02, max(y_data)])
        line_x = np.linspace(0, max(x_data))
        line_y = [limit_func(j, *popt) for j in line_x]
        y_pred = [limit_func(i, *popt) for i in x_data]
        std_dev = np.std(y_data)
        mse = mean_squared_error(y_data, y_pred)
        mae = mean_absolute_error(y_data, y_pred)

        plt.scatter(x_data, y_data, marker='o', color='black')
        plt.plot(line_x, line_y, color='#377eb8', lw=3)
        plt.title(point_name)
        plt.xlabel('delay (milliseconds)')
        plt.ylabel('intensity')
        plt.text(max(x_data), min(line_y), horizontalalignment='right',
                 verticalalignment='bottom',
                 s="B = {:.6f}\nST DEV = {:.6f}\nMSE = {:.6f}\nMAE = {:.6f}"
                 .format(popt[1], std_dev, mse, mae), weight='bold')
        plt.savefig(point_name + '.pdf')

        plt.clf()

    except RuntimeError:
        print(f'RuntimeError: Could not find limit for {point_name}')
        pass
