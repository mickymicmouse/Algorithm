import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
m = list(map(str,input().strip()))
t = n*3

visit = [0]*t
seq = dict()
seq['B']='L'
seq['L']='D'
seq['D']='B'

start=[]
if m[0]=='B':
    start.append((0,1))
if m[-1]=='B':
    start.append((t-1,-1))

if not start:
    print(0)
    exit()

def bfs(x,di):
    q = deque()
    q.append((x, 'B', di))
    visit[x]=1
    while q:
        x, time, di = q.popleft()
        if di==1:
            nx = x+1
            if 0<=nx<t and seq[time]==m[nx]:
                if visit[nx]<visit[x]+1:
                    visit[nx]=visit[x]+1
                    q.append((nx,m[nx], 1))
            nx = 
            

        elif di==-1:



        nx = x+1
        if 0<=nx<t and seq[time]==m[nx]:
            if visit[nx]<visit[x]+1:
                visit[nx]= visit[x]+1
                q.append((nx, m[nx]))
        
        nx = x-1
        if 0<=nx<t and seq[time]==m[nx]:
            if visit[nx]<visit[x]+1:
                visit[nx]=visit[x]+1
                q.append((nx, m[nx]))
    
    return max(visit)
result=-1
for i,di in start:
    result = max(result, bfs(i, di))
print(result)