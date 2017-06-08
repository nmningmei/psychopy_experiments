# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:30:35 2017

@author: ning
"""
import numpy as np
import pandas as pd
from collections import Counter


def make_equal(temp,deviation_count,deviationAway):
    while np.std(deviation_count) >2.5:
        temp = np.random.choice(deviationAway,size=temp.size,replace=True,)
        deviation_count = [v for v in dict(Counter(temp)).values()]
        
    return temp
def correct_response(x):
    if x > 0:
        return 'right'
    elif x < 0:
        return 'left'
    else:
        return 'up'
        
totalTrials = 800
numberofLines = 101
conditions= [0,45,90,135]
deviationAway=np.linspace(-5,5,11)*2
deviationAway=deviationAway[deviationAway!=0]
ones = np.ones(int(totalTrials/len(conditions)/4)) # 25% match
zeros= np.zeros(int(totalTrials/len(conditions)/4*3)) # 75% mismatch
matchCondition = np.array(conditions * int(totalTrials/len(conditions)*0.25))
df_match = pd.DataFrame({'conditions':matchCondition,
             'match':np.ones(matchCondition.shape),
             'deviationAway':np.zeros(matchCondition.size)})
mistmatchCondition = np.array(conditions * int(totalTrials/len(conditions)*0.75))
temp = np.random.choice(deviationAway,size=mistmatchCondition.size,replace=True,)
deviation_count = [v for v in dict(Counter(temp)).values()]
temp = make_equal(temp,deviation_count,deviationAway)
df_mismatch = pd.DataFrame({'conditions':mistmatchCondition,
             'match':np.zeros(mistmatchCondition.shape),
             'deviationAway':temp
        })
experimentmatrix = pd.concat([df_match,df_mismatch])
experimentmatrix['gabor'] = experimentmatrix['conditions'] + experimentmatrix['deviationAway']
experimentmatrix['corrAns'] = experimentmatrix['deviationAway'].apply(correct_response)
experimentmatrix = experimentmatrix.sample(frac=1).reset_index(drop=True)
experimentmatrix.to_csv('D:/NING - spindle/psychopy_experiments/experiment matrix.csv',index=False)
