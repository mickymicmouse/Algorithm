import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split(' '))
sq = [list(map(int,input().split(' '))) for _ in range(n)]
h,w,sr,sc,fr,fc = map(int,input().split(' '))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 1 -> 오른쪽
# 2 -> 왼쪽
# 3 -> 위쪽
# 4 -> 아래쪽

def bfs(x,y):
    dp = [[float('inf')]*(m) for _ in range(n)]
    q=deque()
    q.append((x,y))
    dp[x][y]=0
    while q:
        x,y = q.popleft()
        if x==fr-1 and y==fc-1:
            return dp[x][y]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            flag=False
            if 0<=nx<n-h+1 and 0<=ny<m-w+1:
                if i==0:
                    for s in range(h):
                        if sq[nx+s][ny+w-1]==1:
                            flag=True
                            break
                elif i==1:
                    for s in range(h):
                        if sq[nx+s][ny]==1:
                            flag=True
                            break

                elif i==2:
                    for s in range(w):
                        if sq[nx][ny+s]==1:
                            flag=True
                            break
                else:
                    for s in range(w):
                        if sq[nx+h-1][ny+s]==1:
                            flag=True
                            break
                if flag==False:
                    if dp[nx][ny]>dp[x][y]+1:
                        dp[nx][ny]=dp[x][y]+1
                        q.append((nx,ny))
    return 0
result = bfs(sr-1,sc-1)
if result==0:
    print(-1)
else:
    print(result)

