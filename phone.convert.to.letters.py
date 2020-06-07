# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 07:30:10 2020

@author: anmol
"""
phone=input("phone :")
digimap={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
    }
output=""
for ch in phone:
    output+=digimap.get(ch,"!")+" "
print(output)




