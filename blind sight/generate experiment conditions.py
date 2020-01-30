# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:30:48 2020

@author: ning
"""
import numpy as np
import pandas as pd

contrasts = np.linspace(0.1,.2,3) # 1 unchange, 0-1 decrease, negative inverted
masks = ['gauss']#,'raisedCos','cross']
opacities = np.linspace(0.5,1,5,3) # 1. opaque to 0 transparent
orientations = np.array([item for item in np.arange(45,180 - 45) if np.abs(item - 90) > 15])
spatial_freqs = np.linspace(0.03,0.06,3) # 256x256 - .03~.06, 128x128 - .06~.1
durations = np.linspace(0.1,1,3)

df = dict(contrast = [],
          mask = [],
          opacity = [],
          orientation = [],
          spatial_freq = [],
          duration = [],
          )
for contrast in contrasts:
    for mask in masks:
        for opacity in opacities:
            for orientation in orientations:
                for spatial_freq in spatial_freqs:
                    for duration in durations:
                        df['contrast'].append(contrast)
                        df['mask'].append(mask)
                        df['opacity'].append(opacity)
                        df['orientation'].append(orientation)
                        df['spatial_freq'].append(spatial_freq)
                        df['duration'].append(duration)
df = pd.DataFrame(df)
df['corrAns'] = df['orientation'].apply(lambda x: 'left' if x > 90 else 'right')
df.to_csv('experiment.csv',index = False)