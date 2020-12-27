from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs():
    check[0][0][1]=1
    while queue:
        x,y,w = queue.popleft()
        
        for s in range(4):
            nx = dx[s]+x
            ny = dy[s]+y
            if 0<=nx<N and 0<=ny<M:
                if square[nx][ny]==1 and w==1:
                    queue.append((nx,ny,w-1))
                    check[nx][ny][w-1]=check[x][y][w]+1
                elif square[nx][ny]==0 and check[nx][ny][w]==0:
                    check[nx][ny][w]=check[x][y][w]+1
                    queue.append((nx,ny,w))

N,M = list(map(int, input().split(' ')))

square = []
queue=deque()
check=[[[0]*2 for i in range(M)] for i in range(N)]

for i in range(N):
    line = list(map(int,input().strip()))
    square.append(line)

queue.append((0,0,1))

bfs()

if check[N-1][M-1][0]==0 and check[N-1][M-1][1]==0:
    print(-1)
elif check[N-1][M-1][0]==0 or check[N-1][M-1][1]==0:
    print(max(check[N-1][M-1][0], check[N-1][M-1][1]))
else:
    print(min(check[N-1][M-1][0], check[N-1][M-1][1]))