from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

sdx = [2,2,-2,-2,1,1,-1,-1]
sdy = [1,-1,1,-1,2,-2,2,-2]

def bfs():
    queue = deque()
    queue.append((0,0,K))
    visited = [[[0]*(31) for i in range(W)] for i in range(H)]
    visited[0][0][K]=1
    while queue:
        x,y,k = queue.popleft()
        if x==H-1 and y ==W-1:
            return visited[x][y][k]-1
        for s in range(4):
            nx = dx[s]+x
            ny = dy[s]+y
            if 0<=nx<H and 0<=ny<W:
                if square[nx][ny]==0 and visited[nx][ny][k]==0:
                    queue.append((nx,ny,k))
                    visited[nx][ny][k]=visited[x][y][k]+1
        if k>0:
            for j in range(8):
                nx = sdx[j]+x
                ny = sdy[j]+y
                if 0<=nx<H and 0<=ny<W:
                    if square[nx][ny]==0 and visited[nx][ny][k-1]==0: # 점프를 사용할 경우 아래 k-1칸이 0인지 확인해주어야함
                        queue.append((nx,ny,k-1))
                        visited[nx][ny][k-1]=visited[x][y][k]+1
    return -1
                



K= int(input())
W,H = map(int,input().split(' '))
square = [list(map(int, input().split(' ')))for _ in range(H)]
result = bfs()
print(result)
