# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:30:35 2017

@author: ning
"""
import numpy as np
import pandas as pd
from collections import Counter



totalTrials = 800
numberofLines = 101
experimentmatrix={}
conditions= [0,45,90,135]
experimentmatrix['conditions']= conditions * int(totalTrials/len(conditions))
deviationAway=np.linspace(-5,5,11)
deviationAway=deviationAway[deviationAway!=0]
ones = np.ones(int(totalTrials/len(conditions)/4))
zeros= np.zeros(int(totalTrials/len(conditions)/4*3))
matchRate = np.random.choice(np.concatenate([ones,zeros]),size=len(ones)+len(zeros),replace=False)
idx0   = np.random.choice(matchRate,size=matchRate.size,replace=False)
idx45  = np.random.choice(matchRate,size=matchRate.size,replace=False)
idx90  = np.random.choice(matchRate,size=matchRate.size,replace=False)
idx135 = np.random.choice(matchRate,size=matchRate.size,replace=False)
matchRateVector = np.concatenate([idx0,idx45,idx90,idx135])















experimentmatrix.to_csv('D:/psychopy experiments/experiment matrix.csv',index=False)
