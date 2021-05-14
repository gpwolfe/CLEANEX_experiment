"""
@author: gpwolfe
"""
import os

import matplotlib.pyplot as plt
import pandas as pd


def read_sl5_files(data_dir=os.getcwd()):
    data1 = pd.read_csv(os.path.join(data_dir,
                                     'SL5_cleanex_normalized.csv'), header=0)
    # data2 = pd.read_csv('sl5_cleanex_normalized2.csv', header=0)
    data3 = pd.read_csv(os.path.join(data_dir,
                                     'sl5_cleanex_normalized3.csv'),header=0)
    return data1, data3


def plot_pairs(seq1, seq2, time1, time2):
    name = seq1.name
    fig, ax = plt.subplots()
    
    ax.scatter(time1, seq1, color='blue', label='RNA')
    ax.scatter(time2, seq2, color='red', label='RNA + protein')
    ax.set_xlabel('time')
    ax.set_ylabel('intensity')
    ax.legend()
    ax.set_title(f'{name}')
    plt.savefig(f'{name}_paired_plot.pdf')
    
def execute_plots():
    data1, data3 = read_sl5_files()
    time1 = data1.iloc[:, 0]
    # time2 = data2.iloc[:, 0]
    time3 = data3.iloc[:, 0]
    pair_ix_13 = [(1, 1), (4, 2), (5, 3)]
    for pair in pair_ix_13:
        seq1 = data1.iloc[:, pair[0]]
        seq2 = data3.iloc[:, pair[1]]
        plot_pairs(seq1, seq2, time1, time3)

if __name__ == '__main__':
    execute_plots()
