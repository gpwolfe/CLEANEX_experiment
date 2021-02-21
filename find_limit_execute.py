"""
@author: gpwolfe
"""
from argparse import ArgumentParser
import sys

from find_limit_line import limit_func, plotty
from find_limit_dataframe import limit_data

directory = "/Users/piper/Code/CLEANEX_experiment_Jones/data_folder"
def execute_limit(directory):
    data, errors = limit_data(directory)
    xs = data['time']

    for point in data.columns[1:]:
        plotty(xs, data[point], point)    

def main(argv):
    parser = ArgumentParser(description = "Plot line of fit for CLEANEX data.")
    parser.add_argument('directory', metavar="DIRECTORY",
                        help="data directory")
    args = parser.parse_args(argv)
    directory = args.directory
    execute_limit(directory)
    
    
if __name__ == '__main__':
    main(sys.argv[1:])