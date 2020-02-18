# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:30:27 2020

@author: ning
"""

import os
from glob import glob

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

sub_name = 'pilot'
working_dir = '../results/'
saving_dir = '../result_figures'
if not os.path.exists(os.path.join(saving_dir,sub_name)):
    os.mkdir(os.path.join(saving_dir,sub_name))
working_data = glob(os.path.join(working_dir,sub_name,'*.csv'))

fig,axes = plt.subplots(figsize = (8,12),
                        nrows = 3,
                        sharex = True,
                        sharey = True,
                        )
for f,ax in zip(working_data,axes.flatten()[:2]): 
    df = pd.read_csv(f)
    ax = sns.barplot(x = 'set_size',
                     y = 'just_press.rt',
                     data = df,
                     ax = ax,
                     seed = 12345,
                     )
    ax.set(xlabel = 'Set Size',
           ylabel = 'Reaction Time (sec)')
fig.savefig(os.path.join(saving_dir,sub_name,'results.jpeg'),
            dpi = 300,
            bbox_inches = 'tight')
    
