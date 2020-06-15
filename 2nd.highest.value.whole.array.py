# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:16:50 2020

@author: anmol
"""
import numpy as np
k = np.array([[ 35,  48,  63],
        [ 60,  77,  96],
        [ 91, 112, 135]])
flat=k.flatten()
flat.sort()
flat
print(flat[-2])
print(np.where(k==flat[-2]))