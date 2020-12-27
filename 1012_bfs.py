# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:53:06 2020

@author: seungjun
"""

dx=[0,0,-1,1]
dy=[-1,1,0,0]


def bfs(x,y,c):
    queue =[]
    queue.append((x,y))
    group[x][y]=1
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if square[nx][ny]==1 and group[nx][ny]==0:
                    queue.append((nx,ny))
                    group[nx][ny]=1
            

N=int(input())
for i in range(N):
    w,h,k = list(map(int,input().split(' ')))
    square = [[0]*w for _ in range(h)]
    group = [[0]*w for _ in range(h)]
    for j in range(k):
        a,b= list(map(int, input().split(' ')))
        square[b][a]=1
    cnt =0
    for s in range(w): #x좌표
        for l in range(h): #y좌표
            if square[l][s]==1 and group[l][s]==0:
                cnt+=1
                bfs(l,s,cnt)
    print(cnt)
    
        