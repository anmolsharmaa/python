# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:02:01 2020

@author: anmol
"""
#person name talk()
class person:
    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"hi im {self.name} !")
        
boy=person("boy")
print(boy.name)
boy.talk()    

joe=person("joe")
print(joe.name)  
joe.talk()  
    

