import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split(' ')) # n행 m열
square = [list(map(int,input().strip())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

s_x=0
s_y=0

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(m):
        if square[i][j]==2:
            s_x,s_y=i,j


def bfs(x,y):
    q=deque()
    q.append((x,y,0))
    visit[x][y]=1
    while q:
        x,y,c = q.popleft()
        if square[x][y] in [3,4,5]:
            print('TAK')
            print(c)
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0 and square[nx][ny]!=1:
                    visit[nx][ny]=1
                    q.append((nx,ny,c+1))
    print('NIE')
    return
bfs(s_x,s_y)