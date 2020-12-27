# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:36:22 2020

@author: seungjun
"""



word = {'ABC':2, 'DEF':3, 'GHI':4,
        'JKL':5, 'MNO':6, 'PQRS':7,
        'TUV':8, 'WXYZ':9}
value=0
number = input()
number=list(number)
for i in number:
    for j in word:
        if i in j:
            value=value+word[j]+1
            
print(str(value))