"""
@author: gpwolfe

Execute find_limit_dataframe.py and find_limit_line.py.

Plot data from a series of files. Each file represents intensity data from a
series of peaks for a single time value. For example, one file might include
intensity data for twelve peaks for time = 20 milliseconds.
Column name should correspond to peak name; plot title will be based on this.

File naming should follow the following conventions:

Data to be plotted: protein_temperature_80ms
    (where 80 is replaced by the appropriate time in milliseconds with "ms"
     appended)
Control data: protein_temperature_control
Error data (currently not implemented): protein_temperature_80msB
    (where 80 is replaced by the appropriate time in milliseconds with "msB"
     appended)

"""
from argparse import ArgumentParser
import sys

from find_limit_line import limit_func, plotty
from find_limit_dataframe import limit_data


def execute_limit(directory):
    """
    Execute data file reading and plotting with line of best fit.

    Plots will be saved to current working directory.

    Parameters
    ----------
    directory : string
        Filepath to directory containing data files.

    Returns
    -------
    None.

    """
    data, errors = limit_data(directory)
    xs = data.index

    for point in data.columns[1:]:
        plotty(xs, data[point], point)


def cleanex_plot(argv):
    """
    Run data file reading and plotting from command line.

    Plots are saved to current working directory.

    Example:
        >>> python3 find_limit_execute.py my_data_directory

    Returns
    -------
    None.

    """
    parser = ArgumentParser(description="Plot line of fit for CLEANEX data.")
    parser.add_argument('directory', metavar="DIR",
                        help="data directory")
    args = parser.parse_args(argv)
    directory = args.directory
    execute_limit(directory)


if __name__ == '__main__':
    cleanex_plot(sys.argv[1:])
