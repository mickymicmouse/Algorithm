import sys
input = sys.stdin.readline
from collections import deque
# 이런 코드를 짜면 시간초과가 뜸
# 브루트포스로 짜야되는 문제인듯
# 접근은 좋았음

n,m=map(int,input().split(' '))
sq=[list(map(int,input().split(' '))) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    global result
    q = deque()
    q.append((x,y))
    dp[x][y]=sq[x][y]
    visit[x][y]=1
    while q:
        x,y = q.popleft()
        if visit[x][y]>=5:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0:
                    visit[nx][ny]= visit[x][y]+1
                    dp[nx][ny]=dp[x][y]+sq[nx][ny]
                    q.append((nx,ny))
                elif visit[nx][ny]==visit[x][y]+1:
                    visit[nx][ny]= visit[x][y]+1
                    dp[nx][ny]=max(dp[x][y]+sq[nx][ny], dp[nx][ny])
                    q.append((nx,ny))
                if visit[nx][ny]==4:
                    result = max(result, dp[nx][ny])


def excase(x,y):
    global result
    
    for i in range(4):
        val = sq[x][y]
        for j in range(4):
            if i==j:
                continue
            else:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:

                    val+=sq[nx][ny]
                else:
                    break
            result=max(val, result)

                

result=0
for i in range(n):
    for j in range(m):
        dp = [[0]*m for _ in range(n)]
        visit = [[0]*m for _ in range(n)]
        bfs(i,j)
        excase(i,j)
print(result)

