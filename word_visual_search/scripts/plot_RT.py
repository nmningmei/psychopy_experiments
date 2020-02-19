# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:30:27 2020

@author: ning
"""

import os
from glob import glob

import pandas as pd
import numpy as np
from psychopy.misc import fromFile

from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

from matplotlib import pyplot as plt
import seaborn as sns

sub_name = 'test'
working_dir = '../results/'
saving_dir = '../result_figures'
if not os.path.exists(os.path.join(saving_dir,sub_name)):
    os.mkdir(os.path.join(saving_dir,sub_name))
psy_data = glob(os.path.join(working_dir,sub_name,'*.psydat'))
working_data = glob(os.path.join(working_dir,sub_name,'*.csv'))

dfs = {}
for f,g in zip(working_data,psy_data):
    df_temp = pd.read_csv(f)
    temp = fromFile(g)
    language = temp.extraInfo['language']
    dfs[language] = df_temp


fig,axes = plt.subplots(figsize = (8,12),
                        nrows = 3,
                        sharey = True,
                        )
for (language),ax in zip(['spanish','basque','mixed'],axes.flatten()[:2]): 
    df = dfs[language]
    ax = sns.barplot(x = 'set_size',
                     y = 'just_press.rt',
                     data = df,
                     ax = ax,
                     seed = 12345,
                     )
    ax.set(
           xlabel = 'Set Size',
           ylabel = 'Reaction Time (sec)')

ax = axes.flatten()[-1]
df = dfs['mixed']
gen = TimeseriesGenerator(df['word_type'].values,
                          df['word_type'].values,
                          length = 1,
                          batch_size = 1,
                          )
context = [False]
for (x_0,x_1) in gen:
    context.append(x_0[0][0]!=x_1[0])
context = np.array(context)
df['Switch'] = context
ax = sns.barplot(x = 'word_type',
                 y = 'just_press.rt',
                 hue = 'Switch',
                 hue_order = [True, False],
                 order = ['Spanish','Basque',],
                 data = df,
                 ax = ax,
                 seed = 12345,
                 )
ax.set(xlabel = 'Language',
       ylabel = 'Reaction Time (sec)')

fig.savefig(os.path.join(saving_dir,sub_name,'results.jpeg'),
            dpi = 300,
            bbox_inches = 'tight')
    

