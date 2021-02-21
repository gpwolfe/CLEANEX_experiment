"""
@author: gpwolfe
"""
import os
import pandas as pd
import re


def limit_data(directory):
    dfs = []
    errors = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if (not file.startswith('.') and not file.endswith('B')
                and not file.endswith('control')):
            time = int(re.findall(r'\d+', file.split('_')[-1])[0])
            data = pd.read_table(path)[['Assign F1', 'Height']]
            data.columns = ["point", time]
            data = (data.T)
            data.columns = [x.strip() for x in data.loc['point']]
            data = data.drop('point')
            dfs.append(data)
        if file.endswith('control'):
            control = pd.read_table(path)[['Assign F1', 'Height']]
            control.columns = ["point", 'control']
            control = (control.T)
            control.columns = [x.strip() for x in control.loc['point']]
            control = control.drop('point').astype('float')

        if file.endswith('B'):
            time = int(re.findall(r'\d+', file.split('_')[-1])[0])
            error = pd.read_table(path)[['Assign F1', 'Height']]
            error.columns = ['point', time]
            error = error.T
            error.columns = [x.strip() for x in error.loc['point']]
            error = error.drop('point')
            errors.append(error)
    df = (pd.concat(dfs).astype('float').divide(control.iloc[0])
          .reset_index(drop=False).rename(columns={'index': 'time'}))
    errors = (pd.concat(errors).astype('float').divide(control.iloc[0])
              .reset_index(drop=False).rename(columns={'index': 'time'}))
    return df, errors
