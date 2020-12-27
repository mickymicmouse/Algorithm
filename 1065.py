# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 22:17:13 2020

@author: seungjun
"""

n = input()
count=0
for i in range(1, int(n)+1):
    if i<=99:
        count += 1
        
    else:
        nums = list(map(int, str(i)))
        if nums[0]-nums[1] == nums[1]-nums[2]:
            count+=1
print(count)