# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:00:37 2020

@author: anmol
"""
weight=int(input("Weight: "))
unit=input("L(lbs) or K(kg)")
if unit.upper()=='L':
    conv=weight*0.4
    print(f"converted weight is {conv}kgs")
    
else:
    conv=weight/0.4
    print(f"converted weight is {conv}lbs")
    
