import sys
input = sys.stdin.readline
from collections import deque

n,m= map(int,input().split(' '))

square = [list(map(int,input().split(' '))) for _ in range(n)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def melt():
    global num
    zero=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c = 0
            if square[i][j]!=0:
                for s in range(4):
                    nx = i+dx[s]
                    ny = j+dy[s]
                    if 0<=nx<n and 0<=ny<m:
                        if square[nx][ny]==0:
                            c+=1

    
                zero[i][j]=c
    for i in range(n):
        for j in range(m):
            val = square[i][j]-zero[i][j]
            if val<=0:
                square[i][j]=0
            else:
                square[i][j]=val
    return

def check(x,y):
    global num
    q=deque()
    q.append((x,y))
    if visit[x][y]==0:
        visit[x][y]=1
        num+=1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if square[nx][ny]!=0 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append((nx,ny))
    return
    

year = 0
while True:
    num = 0
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if square[i][j]!=0 and visit[i][j]==0:
                check(i,j)
                
    if num>=2:
        print(year)
        break
    if num==0:
        print(0)
        break
    year+=1
    melt()

