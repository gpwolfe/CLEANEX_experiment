#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:12:46 2021

@author: piper
"""
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# The third value in popt (corresponding to 'c' in the
# function fed to curve_fit) is the upper asympototic limit.

# c-a ('a' being the first value in popt) gives the y-intercept,
# which is close to 0 in most cases in these experiments.

# 'b', the second value in popt, defines the rate of decay of the
# subtracted term 'a'. At first, 'a' is about as large as 'c', but as the
# 'x' term grows larger, the function subtracts less and less from 'c',
# with 'b' defining this interaction.


def func(x, a, b, c):
    """Function for limit line."""
    return c-(a * np.exp(-b*x))


def plotty(x_data, y_data, point_name):
    """
    Takes a two arrays, one corresponding to delay in milliseconds, the other
    corresponding to the measured peak intensity. Produces a graph with the
    data points, a line of best fit, the upper limit, and the B value, which
    corresponds to the rate of deceleration of the rate of increase (that is,
    how quickly the line of fit bends to horizontal).

    line_x: 2D array-like, matches length of y_data
    line_y: 2D array-like, matches length of x_data
    point_name: String, plot title and file name, e.g. "Arginine_298K_azara"

    example: plotty(range(0,200))
    """

    # Generating line of fit for experimental data
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
