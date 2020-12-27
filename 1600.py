# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:15:03 2020

@author: seungjun
"""

import copy

def judge(value, height, width, w, h, s):


    
    if width ==0 and height ==0:
        return 0, s
    if width==1 and height ==0:
        return 1, s
    if width==0 and height==1:
        return 1, s
    if width==1 and height==1:
        up = value[height-1][width][0]
        left = value[height][width-1][0]
        if up==10000 and left==10000:
            return 10000, s
        else:
            
            return 2, s
    
    if width==0:
        up = value[height-1][width][0]
        return up+1, s
    if height==0:
        left = value[height][width-1][0]
        return left+1, s

    
    if height==1:
        value2=10000
        if value[height-1][width-2][1]!=0 and value[height-1][width-2][0]!=10000:
            value2 = value[height-1][width-2][0]    

        left=value[height][width-1][0]
        up = value[height-1][width][0]
        
        sk=[value[height-1][width-2][1]-1, value[height][width-1][1],value[height-1][width][1]]
        pre = [value2,left,up] 
        minis=pre.index(min(pre))
        
        
        return min(pre)+1,sk[minis] 
    
    
    elif width==1:
        value1=10000
        if value[height-2][width-1][1]!=0 and value[height-2][width-1][0]!=10000:
            value1 = value[height-2][width-1][0]
        left=value[height][width-1][0]
        up = value[height-1][width][0]
        
        sk=[value[height-2][width-1][1]-1, value[height][width-1][1],value[height-1][width][1]]
        pre = [value1,left,up] 
        minis=pre.index(min(pre))
        
        
        return min(pre)+1,sk[minis]
        
        
    else:
        value1=10000
        value2=10000
        if value[height-2][width-1][1]!=0 and value[height-2][width-1][0]!=10000:
            value1 = value[height-2][width-1][0]
        if value[height-1][width-2][1]!=0 and value[height-1][width-2][0]!=10000:
            value2 = value[height-1][width-2][0]    
        
        left=value[height][width-1][0]
        up = value[height-1][width][0]
        
        sk=[value[height-2][width-1][1]-1, value[height-1][width-2][1]-1, value[height][width-1][1],value[height-1][width][1]]
        pre = [value1,value2,left,up] 
        minis=pre.index(min(pre))
        
        
        return min(pre)+1,sk[minis] 

k=int(input())
w,h=input().split(' ')
w=int(w)
h=int(h)
base=[[0]*w]*h
for i in range(h):
    base[i] = input().split(' ')
    
value=copy.deepcopy(base)

dis=w+h
count=0
skill=k

for i in range(h):
    for j in range(w):
        
        if base[i][j]=='1':
            value[i][j]=10000,skill
        else:
            value[i][j] = judge(value, i, j , w, h, skill)
        

if value[h-1][w-1][0]>=10000:
    print(-1)        
else:
    print(value[h-1][w-1][0])
    

   
