# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:35:40 2020

@author: seungjun
"""

N= int(input())

square=[]
for i in range(N):
    line = list(map(int, input()))
    square.append(line)
    
group = [[0]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,c):
    queue=[]
    queue.append((x,y)) # 큐에 현재 좌표 입력
    group[x][y]=c # 그룹 설정
    while queue: #큐가 존재하면
        x,y = queue.pop(0) #큐안의 왼쪽값부터 추출
        for i in range(4):
            nx=x+dx[i] #왼쪽 오른쪽 위 아래 순서대로 움직이면서 
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N: # 맵안에 있는 값이면서
                if square[nx][ny]==1 and group[nx][ny]==0: # 아파트가 있고, 그룹설정이 되지 않은 곳이라면
                    queue.append((nx,ny)) # 큐에 넣고
                    group[nx][ny]=c # 단지로 설정해준다.

cnt=0

for a in range(N):
    for b in range(N): # 모든 맵을 돌면서
        if square[a][b]==1 and group[a][b]==0: # 아파트가 있는데 단지설정이 안된 곳이라면
            cnt+=1 
            bfs(a,b,cnt) # bfs 실행
            
print(cnt)
flat=[]
for x in group:
    flat.extend(x)
numlist=[]    
for i in range(cnt):
    numlist.append(flat.count(i))
numlist.sort()
print(numlist)