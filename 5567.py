# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 16:00:29 2020

@author: seungjun
"""


a=int(input())
b=int(input())
k=[]
for i in range(int(b)):
    ss = input()
    splits = ss.split(' ')
    k.append(splits)

friends=[]
invite =[]
for i in range(len(k)):
    if int(k[i][0]) == 1:

        friends.append(int(k[i][1]))
        invite.append(int(k[i][1]))
    elif int(k[i][1])==1:
        friends.append(int(k[i][0]))
        invite.append(int(k[i][0]))        
        
for i in range(len(k)):
    for j in range(len(friends)):
        if int(k[i][0]) == int(friends[j]) and int(k[i][1]) not in invite and int(k[i][1])!=1:
            invite.append(int(k[i][1]))
            
        elif int(k[i][1]) == int(friends[j]) and int(k[i][0]) not in invite and int(k[i][0])!=1:
            invite.append(int(k[i][0]))
            
print (len(invite))
