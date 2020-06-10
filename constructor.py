# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:05:10 2020

@author: anmol
"""
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):  
        print("draw")

point1=point(10,20)
print(point1.x)
print(point1.y)
point1.draw()
point1.move()

point2=point(30,40)
print(point2.x)
print(point2.y)
point2.draw()
point2.move()




