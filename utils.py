# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:04:54 2020

@author: anmol
"""

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
     if number > max:
        max = number
     return max        

