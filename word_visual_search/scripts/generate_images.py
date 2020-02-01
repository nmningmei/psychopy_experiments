# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:56:33 2020

@author: ning
"""

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist

from utils import single_langauge,switching_language

working_data = '../data/SEMGEN_Final_Stimuli.csv'
df = pd.read_csv(working_data,sep = ';',encoding='latin-1')

n_distractors = np.arange(4,29,4)
n_trials = 60
grid_size = 12
tol = 0.08

# single langage -- no switch
## spanish - target, basque - distractor
target,distractor = ['Spanish','Basque']

df_to_save = single_langauge(df,target,distractor,
                     n_distractors = n_distractors,
                     n_trials = n_trials,
                     grid_size = grid_size,
                     tol = tol,)
df_to_save.to_csv(f'../data/{target}.csv',index = False)

## basque - target,spanish - distractor
target,distractor = ['Basque','Spanish',]

df_to_save = single_langauge(df,target,distractor,
                     n_distractors = n_distractors,
                     n_trials = n_trials,
                     grid_size = grid_size,
                     tol = tol,)
df_to_save.to_csv(f'../data/{target}.csv',index = False)


# switching
df_spanish_basque = switching_language(df,'Spanish','Basque',
                     n_distractors = n_distractors,
                     n_trials = int(n_trials/2),
                     grid_size = grid_size,
                     tol = tol,)
df_spanish_basque['target_language'] = 'Spanish'
df_basque_spanish = switching_language(df,'Basque','Spanish',
                     n_distractors = n_distractors,
                     n_trials = int(n_trials/2),
                     grid_size = grid_size,
                     tol = tol,)
df_basque_spanish['target_language'] = 'Basque'
df_to_save = pd.concat([df_spanish_basque,
                        df_basque_spanish,])
df_to_save.to_csv('../data/mixed.csv',index = False)






























