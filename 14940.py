import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split(' '))
sq = [list(map(int,input().split(' '))) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

dp = [[float('inf')]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if sq[i][j]==2:
            x,y = i,j
        elif sq[i][j]==0:
            dp[i][j]=0


def bfs(x,y):
    q=deque()
    q.append((x,y))
    dp[x][y]=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and sq[nx][ny]==1:
                if dp[nx][ny]>dp[x][y]+1:
                    dp[nx][ny]=dp[x][y]+1
                    q.append((nx,ny))




bfs(x,y)

for i in range(n):
    for j in range(m):
        if dp[i][j]==float('inf'):
            dp[i][j]=-1
        print(dp[i][j], end=' ')
    print()



