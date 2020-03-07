import os

import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv


column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = read_csv('~/Desktop/Boston/housing.data', header=None, delimiter=r"\s+", names=column_names)

os.makedirs('plots/Homework7', exist_ok=True)


for col1_idx, column1 in enumerate(data.columns):
    for col2_idx, column2 in enumerate(data.columns):
        if col1_idx < col2_idx:
            print(f'Generating {column1} to {column2} plot')
            fig, axes = plt.subplots(1, 1, figsize=(5, 5))
            axes.scatter(data[column1], data[column2], label=f'{column1} to {column2}', color='r', marker='.',alpha=1)
            axes.set_title(f'{column1} to {column2}')
            axes.set_xlabel(column1)
            axes.set_ylabel(column2)
            axes.legend()
            plt.savefig(f'plots/Homework7/boston_{column1}_{column2}_scatter.png', dpi=300)
            plt.close(fig)

plt.close()
