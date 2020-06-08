# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:45:16 2020

@author: anmol
"""
try:
    age=int(input("age: "))
    print(age)
except ValueError:
    print("invalid value")
