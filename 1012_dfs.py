# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:22:36 2020

@author: seungjun
"""

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,c):
    group[x][y]=1
    for j in range(4):
        nx = dx[j]+x
        ny = dy[j]+y
        
        if 0<=nx<h and 0<=ny<w:
            if square[nx][ny]==1 and group[nx][ny]==0:
                dfs(nx,ny,c)


N=int(input())
for i in range(N):
    w,h,k=list(map(int,input().split(' ')))
    square = [[0]*w for _ in range(h)]
    group = [[0]*w for _ in range(h)]
    
    for _ in range(k):
        x,y = list(map(int, input().split(' ')))
        square[y][x]=1
    cnt = 0
    for first in range(h):
        for second in range(w):
            if square[first][second]==1 and group[first][second]==0:
                cnt+=1
                dfs(first, second, cnt)
                
    print(cnt)
    
    
