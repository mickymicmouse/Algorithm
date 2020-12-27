# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:41:09 2020

@author: seungjun
"""


# 최단 경로 문제는 DFS로 풀수 없다 중요!
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(x,y,c):
    group[x][y]=1
    global nums
    if square[x][y]==1:
        nums+=1
    for s in range(4):
        nx = dx[s]+x
        ny = dy[s]+y
        if 0<=nx<N and 0<=ny<M:
            if square[nx][ny]==1 and group[nx][ny]==0:
                dfs(nx,ny,c)
                



N,M = list(map(int,input().split(' ')))

group = [[0]*M for _ in range(N)]
square = []
for i in range(N):
    line = list(map(int, input()))
    square.append(line)
    
nums=1
cnt=0
for i in range(N):
    for j in range(M):
        if square[i][j]==1 and group[i][j]==0:
            cnt+=1
            dfs(i,j,cnt)
            
print(cnt)

