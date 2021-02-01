import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int, input().split(' '))
n,m = map(int,input().split(' '))
match = dict()
visit = [0]*n
for i in range(n):
    match[i+1]=[]
for i in range(m):
    x,y = map(int,input().split(' '))
    match[x].append(y)
    match[y].append(x)

result = float('inf')
def bfs(x):
    q=deque()
    q.append((x,0))
    visit[x-1]=1
    while q:
        x, idx = q.popleft()
        if x==b:
            print(idx)
            return
        for nx in match[x]:
            if visit[nx-1]==0:
                q.append((nx,idx+1))
                visit[nx-1]=1
    print(-1)
    return

bfs(a)