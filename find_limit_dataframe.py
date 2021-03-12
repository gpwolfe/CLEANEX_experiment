"""
@author: gpwolfe

Read data files and return data for plotting by find_limit_line.py. Executed
by find_limit_execute.py

File naming should follow the following conventions:

Data to be plotted: protein_temperature_80ms
(where 80ms is replaced by the appropriate time in milliseconds with "ms"
appended)

Control data: protein_temperature_control

Error data (currently not implemented on plot): protein_temperature_80msB
(where 80msB is replaced by the appropriate time in milliseconds with "msB"
appended)
"""

import os
import re

import pandas as pd

FILENAME_RE = re.compile(
        r'\A\S+_((?P<time>\d+)ms(?P<error>B)?|(?P<control>control))\Z')


def limit_data(directory):
    """
    Read data files from directory and return dataframe of values to plot.

    Example:
        data, errors = limit_data(my_data_directory)

    Parameters
    ----------
    directory : string
        Filepath to directory containing data files.

    Returns
    -------
    df : pandas.DataFrame
        Dataframe containing peak intensity values to be plotted, indexed by
        time in milliseconds (index) and peak name (columns).
    error_df : pandas.DataFrame
        Dataframe containing values for setting errorbars on plot.
    """
    dfs = []
    errors = []

    for fn in os.listdir(directory):
        match = FILENAME_RE.match(fn)
        if not match:
            continue

        is_err = match.group('error')
        is_control = match.group('control')
        time_str = match.group('time')
        if time_str:
            time_int = int(time_str)

        path = os.path.join(directory, fn)
        data = pd.read_table(path)[['Assign F1', 'Height']]
        data.index = [x.strip() for x in data['Assign F1']]
        data.drop('Assign F1', axis=1, inplace=True)

        if is_control:
            control = data.astype('float')
        elif time_str:
            data.columns = [time_int]
            if is_err:
                errors.append(data)
            else:
                dfs.append(data)
        else:
            print(f'{fn} not processed.')
            continue

    df = (pd.concat(dfs, axis=1).astype('float')
          .divide(control.iloc[:, 0], axis=0).T)
    df = df.append(pd.Series(0, index=df.columns, name=0))
    error_df = (pd.concat(errors, axis=1).astype('float')
                .divide(control.iloc[:, 0], axis=0))

    return df, error_df
