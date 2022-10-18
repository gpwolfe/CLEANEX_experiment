# CLEANEX_experiment
Plotting RNA data from NMR experiments analyzed using [CcpNmr](www.ccpn.ac.uk) with line fitting based on millisecond time scale and collected peak 
intensity values.

## Requirements
Python 3 (created using Python 3.8)

Libraries: matplotlib, pandas, scikit-learn, scipy

## Usage
Data to be plotted should be saved in comma-separated values (.csv) format.

Each file should represent peak values from all analyzed peaks for one time value (i.e. when plotting ten peaks, intensity values for all ten peaks
at 10ms should be contained in one file. Intensity values for all ten peaks at 20ms should be contained in a separate file).

File names should follow these conventions:

Data files:
name_temperature_XXms  
Where XX is replaced by the time in milliseconds.

Example: Arg29_280K_80ms

Control data (used for normalization):
name_temperature_control

Example: Arg29_280K_control

Files to be plotted, including control file, should be contained in the same directory. Ideally, directory should have no other contents.

From the command line, run the following:

`python3 find_limit_execute.py path/to/data_directory`

## Output
Individual scatter plots for each peak, corresponding to intensity values (y-axis) across increasing time (x-axis).

A line of best fit is plotted, using the function C-(A ^ (-B*X))

The fitted line should resemble a curve starting near zero, approaching some y-value.

Text on the plot includes:

- The value for B, which moderates the rate of increase as the line of fit approaches some upper limit

- Mean squared error (MSE) of line of fit

- Mean absolute error (MAE) of line of fit

Plots will be saved in .pdf format to current working directory.
