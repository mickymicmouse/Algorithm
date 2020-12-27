# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:46:28 2020

@author: seungjun
"""




#반복 for
k=1
for i in range(int(a),0,-1):
    k *= i
    
    
#재귀
a = input()
def factorial(c):
    if c==0:
        return 1
    if c==1:
        return 1
        
    return c*factorial(c-1) 
print(factorial(int(a)))