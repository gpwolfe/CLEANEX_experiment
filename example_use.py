#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:23:28 2021

@author: piper
"""
import pandas as pd
import matplotlib.pyplot as plt
from find_limit_line import *

"""
Before using plotty, your data should be in .csv format (or other
pandas.read_csv() compatible format).

An example of how to use plotty follows:
The first column of your data is labeled "time". This is the time in
milliseconds, i.e., [0, 10, 20, 40, 60, 80, 100, 120, 150, 200].

The other columns each correspond to the data from one peak. One column might
thus be: [0, 0.14, 0.30, 0.36, 0.39, 0.42, 0.38, 0.39, 0.35, 0.35].

The label of each of these columns should identify the peak in a unique way.
Plotty uses the column labels as part of the file name and plot title.

The for-loop example below will iterate across each peak column and generate
a plot, if possible.

The variable "name" is used to assign plot titles and filenames in a
consistent way.
"""

arginine_1 = pd.read_csv('arginine_1.csv')

xs = arginine_1.time


for column in range(1, arginine_1.shape[1]):
    try:
        name = "Arginine 1 at 280K " + arginine_1.columns[column]
        plotty(xs, arginine_1.iloc[:, column], name)
    except RuntimeError:
        print("Error, cannot fit. Continuing.")
        continue
