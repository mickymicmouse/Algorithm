
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y, c):
    queue = []
    queue.append((x,y))
    visited[x][y]=1
    while queue:
        x,y = queue.pop(0)
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            if 0<=nx<N and 0<=ny<M:
                if square[nx][ny]==1 and visited[nx][ny]==0:
                    
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
                    



N,M = list(map(int,input().split(' ')))
square = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    line=list(map(int,input()))
    square.append(line)
cnt =0
bfs(0,0,cnt)
print(visited[N-1][M-1])
