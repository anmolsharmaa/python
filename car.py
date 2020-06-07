# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:51:50 2020

@author: anmol
"""
print('type help : ')
j=0
while j<10:
    k=input()
    j+=1
    if k.lower() =='help':
     print('''
    start-to start the car 
    stop- to stop the car 
    quit- to exit         ''')
     break
    else:
     print('no bruh type help nothin else')
     

i=0
while i<10:
    x=input("command: ")
    i+=1
    if x.lower()=='start':
     print('the car started ready to go')
    elif x.lower()=='stop':
        print('car stopped')
    elif x.lower()=='quit' :
        print('thanks for playing')
        break
    else:
        print('choose only from the commands bruh')
            
        
    
    
    
    
    
    