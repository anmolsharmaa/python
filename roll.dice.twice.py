# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:36:55 2020

@author: anmol
"""
import random

class Dice:
    def roll(self):
        first= random.randint(1,6)
        second=random.randint(1,6)
        return first,second 
    
dice = Dice() 
print(dice.roll())   