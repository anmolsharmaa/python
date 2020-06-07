# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 07:43:56 2020

@author: anmol
"""
message=input("type ur msg with emoji :")
words=message.spit(' ')
emojis={
        ":)":"\U0001F642",
        ":(":"\U0001F614",
        ";)":"\U0001F609",
        }
output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)
