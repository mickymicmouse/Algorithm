# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:58:17 2020

@author: seungjun
"""

a = input()

def fibonacchi(a):
    if a ==0:
        return 0
    elif a==1:
        return 1
    elif a==2:
        return 1
    
    return fibonacchi(a-2)+fibonacchi(a-1)
print(fibonacchi(int(a)))