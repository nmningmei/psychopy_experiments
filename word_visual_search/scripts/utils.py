# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:07:54 2020

@author: ning
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial.distance import pdist
from sklearn.utils import shuffle
from tqdm import tqdm

def single_langauge(df,
                    target,
                    distractor,
                    n_distractors = [],
                    n_trials = 60,
                    tol = 0.08,
                    grid_size = 12,
                    search = int(1e4),
                    high = 2,
                    low = 0,
                    font_size = 14,
                    ):
    targets = df[target].values.copy()
    distractor = df[distractor].values.copy()
    
    np.random.seed(12345)
    set_sizes = np.random.choice(n_distractors,size = n_trials,)
    positions = []
    for set_size in set_sizes:
        temp = np.random.uniform(low,high,size = (set_size + 1,2))
        if pdist(temp).min() < tol:
            for _ in tqdm(range(search)):
                temp = np.random.uniform(low,high,size = (set_size + 1,2))
                if pdist(temp).min() >= tol:
                    break
        print(pdist(temp).min())
        positions.append(temp)
    
    res = dict(trial = [],
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
                    fontsize = font_size,
                    rotation = rotation,
                    )
        ax.set(xlim=(0,grid_size),
               ylim=(0,grid_size))
        ax.axis('off')
        fig.savefig(f'../figures/{target}_{ii}.jpeg',
                    bbox_inches = 'tight',)
        plt.close('all')
        
        res['trial'].append(ii)
        res['set_size'].append(set_size)
        res['target_word'].append(target_word)
        res['distract_words'].append(','.join(list(distract_word)))
        res['image_path'].append(f'../figures/{target}_{ii}.jpeg')
    return pd.DataFrame(res)

def switching_language(df,
                    set_size = 8,
                    n_trials = 60,
                    tol = 0.08,
                    grid_size = 12,
                    search = int(1e4),
                    high = 2,
                    low = 0,
                    font_size = 14,
                    ):
    positions = []
    for ii in range(n_trials):
        temp = np.random.uniform(low,high,size = (set_size + 1,2))
        if pdist(temp).min() < tol:
            for _ in tqdm(range(search)):
                temp = np.random.uniform(low,high,size = (set_size + 1,2))
                if pdist(temp).min() >= tol:
                    break
        positions.append(temp)
    
    np.random.seed(12345)
    basque_words = np.random.choice(df['Basque'].values,
                                    size = int(len(positions) / 2),
                                    replace = False,)
    spanish_words = np.random.choice(df['Spanish'].values,
                                     size = int(len(positions) /2),
                                     replace = False)
    sampled_words = np.concatenate([basque_words,spanish_words])
    word_type = np.concatenate([['Basque']*basque_words.shape[0],
                                ['Spanish']*spanish_words.shape[0]])
    sampled_words,word_type = shuffle(sampled_words,word_type)
    
    res = dict(trial = [],
              set_size = [],
              target_word = [],
              distract_words = [],
              image_path = [],
              )
    for ii,(position,sampled_word,word_type_) in enumerate(zip(positions,sampled_words,word_type)):
        target_col = word_type_
        distractor_col = list(
                    set(['Spanish','Basque']).symmetric_difference(set([target_col])))[0]
        targets = df[target_col].values.copy()
        distractor = df[distractor_col].values.copy()
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
                    fontsize = font_size,
                    rotation = rotation,
                    )
        ax.set(xlim=(0,grid_size),
               ylim=(0,grid_size))
        ax.axis('off')
        fig.savefig(f'../figures/mixed_{ii}.jpeg',
                    bbox_inches = 'tight',)
        plt.close('all')
        
        res['trial'].append(ii)
        res['set_size'].append(set_size)
        res['target_word'].append(target_word)
        res['distract_words'].append(','.join(list(distract_word)))
        res['image_path'].append(f'../figures/mixed_{ii}.jpeg')
        
    
    return pd.DataFrame(res)