# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:03:43 2020

@author: seungjun
"""

n,m = input().split(' ')
n=int(n)
m=int(m)
s=input().split(' ')
score=[]
for i in range(len(s)):
    score.append(int(s[i]))
maximum=0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            value = score[i]+score[j]+score[k]
            if value <= m and value>maximum:
                maximum=value
print(maximum)