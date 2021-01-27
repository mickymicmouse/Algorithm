import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split(' '))
r = dict()
for i in range(n):
    r[i+1]=[]
for i in range(m):
    a,b = map(int,input().split(' '))
    r[a].append(b)

def bfs(x):
    dp = [float('inf')]*n
    q=deque()
    q.append(x)
    dp[x-1]=0
    while q:
        x = q.popleft()
        for nx in r[x]:
            if dp[nx-1]>dp[x-1]+1:
                dp[nx-1]=dp[x-1]+1
                q.append(nx)
    return dp
count=0
dp = bfs(x)
for i in range(len(dp)):
    if dp[i]==k:
        count+=1
        print(i+1)
if count==0:
    print(-1)