import sys
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():

    while queue:
        x,y=queue.popleft()
        for s in range(4):
            nx = dx[s]+x
            ny = dy[s]+y
            if 0<=nx<N and 0<=ny<M:
                if square[nx][ny]==0 and check[nx][ny]==0 and square[nx][ny]==0:
                    queue.append((nx,ny))
                    square[nx][ny]= square[x][y]+1
            
M,N = list(map(int, input().split(' ')))
square = []
check = [[0]*M for _ in range(N)]
num_zeros=0
for i in range(N):
    line = list(map(int,input().split(' ')))
    num_zeros += line.count(0)
    square.append(line)

if num_zeros==0:
    print(0)
    exit()
queue = deque()
for i in range(N):
    for j in range(M):
        if square[i][j]==1:
            queue.append((i,j))

bfs()

result = -10
for i in square:
    for j in i:
        if j==0:
            print(-1)
            exit()
        result=max(result,j)

print(result-1)