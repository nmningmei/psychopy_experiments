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
df_words = pd.read_csv(working_data,sep = ';',encoding='latin-1')

n_distractors = np.arange(2,16,3)
n_trials = 60
grid_size = 10
tol = 0.7
font_size = 16

# single langage -- no switch
# spanish - target, basque - distractor
target,distractor = ['Spanish','Basque']

df_to_save = single_langauge(df_words,target,distractor,
                     n_distractors = n_distractors,
                     n_trials = n_trials,
                     grid_size = grid_size,
                     tol = tol,
                     font_size = font_size,
                     )
df_to_save.to_csv(f'../data/{target}.csv',index = False)

## basque - target,spanish - distractor
target,distractor = ['Basque','Spanish',]

df_to_save = single_langauge(df_words,target,distractor,
                     n_distractors = n_distractors,
                     n_trials = n_trials,
                     grid_size = grid_size,
                     tol = tol,
                     font_size = font_size,
                     )
df_to_save.to_csv(f'../data/{target}.csv',index = False)


# switching
df_to_save = switching_language(df_words,
                    set_size = 8,
                    n_trials = n_trials,
                    tol = tol,
                    grid_size = grid_size,
                    font_size = font_size,
                    )
df_to_save.to_csv('../data/mixed.csv',index = False)






























