# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:07:54 2020

@author: ning
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist

def single_langauge(df,
                    target,
                    distractor,
                    n_distractors = [],
                    n_trials = 60,
                    tol = 0.08,
                    grid_size = 12,
                    ):
    targets = df[target].values.copy()
    distractor = df[distractor].values.copy()
    
    np.random.seed(12345)
    set_sizes = np.random.choice(n_distractors,size = n_trials,)
    positions = []
    for set_size in set_sizes:
        temp = np.random.rand(set_size + 1,2)
        if pdist(temp).min() < tol:
            for _ in range(int(1e5)):
                temp = np.random.rand(set_size + 1,2)
                if pdist(temp).min() >= tol:
                    break
        positions.append(temp)
    
    df = dict(trial = [],
              set_size = [],
              target_word = [],
              distract_words = [],
              image_path = [],
              )
    for ii,(set_size,position) in enumerate(zip(set_sizes,positions)):
        target_word = np.random.choice(targets,size = 1)
        distract_word = np.random.choice(distractor,
                                         size = set_size,
                                         replace = False,)
        words = np.concatenate([target_word,distract_word])
        rotations = np.random.randint(-35,35,size = len(words))
        plt.close('all')
        fig,ax = plt.subplots(figsize=(grid_size,grid_size))
        for word,(x,y),rotation in zip(words,position,rotations):
            ax.text(x * grid_size,
                    y * grid_size,
                    word,
                    ha = 'center',
                    fontsize = 14,
                    rotation = rotation,
                    )
        ax.set(xlim=(0,grid_size),
               ylim=(0,grid_size))
        ax.axis('off')
        fig.savefig(f'../figures/{target}_{ii}.jpeg',
                    bbox_inches = 'tight',)
        plt.close('all')
        
        df['trial'].append(ii)
        df['set_size'].append(set_size)
        df['target_word'].append(target_word)
        df['distract_words'].append(','.join(list(distract_word)))
        df['image_path'].append(f'../figures/{target}_{ii}.jpeg')
    return pd.DataFrame(df)

def switching_language(df,
                    target_col,
                    distractor_col,
                    n_distractors = [],
                    n_trials = 60,
                    tol = 0.08,
                    grid_size = 12,
                    ):
    targets = df[target_col].values.copy()
    distractor = df[distractor_col].values.copy()
    
    np.random.seed(12345)
    set_sizes = np.random.choice(n_distractors,size = n_trials,)
    positions = []
    for set_size in set_sizes:
        temp = np.random.rand(set_size + 1,2)
        if pdist(temp).min() < tol:
            for _ in range(int(1e5)):
                temp = np.random.rand(set_size + 1,2)
                if pdist(temp).min() >= tol:
                    break
        positions.append(temp)
    
    df = dict(trial = [],
              set_size = [],
              target_word = [],
              distract_words = [],
              image_path = [],
              )
    for ii,(set_size,position) in enumerate(zip(set_sizes,positions)):
        target_word = np.random.choice(targets,size = 1)
        distract_word = np.random.choice(distractor,
                                         size = set_size,
                                         replace = False,)
        words = np.concatenate([target_word,distract_word])
        rotations = np.random.randint(-35,35,size = len(words))
        plt.close('all')
        fig,ax = plt.subplots(figsize=(grid_size,grid_size))
        for word,(x,y),rotation in zip(words,position,rotations):
            ax.text(x * grid_size,
                    y * grid_size,
                    word,
                    ha = 'center',
                    fontsize = 14,
                    rotation = rotation,
                    )
        ax.set(xlim=(0,grid_size),
               ylim=(0,grid_size))
        ax.axis('off')
        fig.savefig(f'../figures/{target_col}_{distractor_col}_{ii}.jpeg',
                    bbox_inches = 'tight',)
        plt.close('all')
        
        df['trial'].append(ii)
        df['set_size'].append(set_size)
        df['target_word'].append(target_word)
        df['distract_words'].append(','.join(list(distract_word)))
        df['image_path'].append(f'../figures/{target_col}_{distractor_col}_{ii}.jpeg')
    return pd.DataFrame(df)