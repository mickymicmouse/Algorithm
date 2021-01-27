import sys
input = sys.stdin.readline
from collections import deque
r = dict()
n,m = map(int, input().split(' '))
for i in range(n):
    r[i+1]=[]
for i in range(m):
    a,b = map(int,input().split(' '))
    r[a].append(b)
    r[b].append(a)
def bfs(x):
    dp = [float('inf')]*n
    q = deque()
    q.append(x)
    dp[x-1]=0
    while q:
        x = q.popleft()
        for nx in r[x]:
            if dp[nx-1]>dp[x-1]+1:
                dp[nx-1]=dp[x-1]+1
                q.append(nx)
    return sum(dp)
result = float('inf')
index = 0
for s in range(1,n+1):
    k = bfs(s)
    if result>k:
        index = s
        result = k
print(index)
