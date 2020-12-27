# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:49:07 2020

@author: seungjun
"""

alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = input()

score=[]
for i in alpha:
    
        
    word = word.replace(i,'a')
        
        
print(len(word))
print(word)