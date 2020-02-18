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

working_dir = '../results/'
working_data = glob(os.path.join(working_dir,'*.csv'))

fig,axes = plt.subplots(figsize = (8,12),
                        nrows = 3)
for f,ax in zip(working_data,axes.flatten()): 
    df = pd.read_csv(f)
    ax = sns.barplot(x = 'set_size',
                     y = 'just_press.rt',
                     data = df,
                     ax = ax,
                     )
    
    
