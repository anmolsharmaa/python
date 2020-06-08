# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:54:19 2020

@author: anmol
"""
try:
    age=int(input("age: "))
    income=20000
    risk=income/age
except ZeroDivisionError:
    print("age cannot be 0")
    
except ValueError:
    print("invalid value")
    
