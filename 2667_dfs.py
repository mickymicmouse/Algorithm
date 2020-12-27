# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 14:51:00 2020

@author: seungjun
"""

N= int(input())

square=[]
for i in range(N):
    line = list(map(int, input()))
    square.append(line)
    
visited = [[0]*N for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,c): 
    visited[x][y]=1
    global nums
    if square[x][y]==1:
        nums+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny] ==0 and square[nx][ny]==1:
                dfs(nx,ny,c)
    
cnt = 1
numlist = []
nums=0
for a in range(N):
    for b in range(N):
        if square[a][b] ==1 and visited[a][b]==0:
            dfs(a,b,cnt)
            numlist.append(nums)
            nums = 0
            cnt += 1

print(len(numlist))
numlist.sort()
for i in numlist:
    print(i)