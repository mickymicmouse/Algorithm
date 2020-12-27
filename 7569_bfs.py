from collections import deque

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for s in range(6):
            nx = dx[s]+x
            ny = dy[s]+y
            nz = dz[s]+z
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and square[nx][ny][nz]==0:
                queue.append((nx,ny,nz))
                square[nx][ny][nz]= square[x][y][z]+1

M,N,H = list(map(int,input().split(' ')))
queue = deque()
square = []
num_zeros=0
for i in range(H):
    square_inner=[]
    for j in range(N):
        line = list(map(int, input().split(' ')))
        num_zeros+=line.count(0)
        square_inner.append(line)
    square.append(square_inner)

if num_zeros==0:
    print(0)
    exit()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if square[i][j][k]==1:
                queue.append((i,j,k))

bfs()

result = -10
for i in square:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit()
            result=max(result, k)
print(result-1)