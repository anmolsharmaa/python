# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 04:33:11 2020

@author: anmol
"""
import numpy as np

c = np.array([[1. ,  0.7,  0.4,  0.1],
              [0.7,  1. ,  0.3,  0.2],
              [0.4,  0.3,  1. ,  0.5],
              [0.1,  0.2,  0.5,  1. ]])
c -= np.eye(c.shape[0])  # remove the 1 on diagonal
result = np.array([[np.max(row), num_row, np.argmax(row)] for num_row, row in enumerate(c)])

print(result)