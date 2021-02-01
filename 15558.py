import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split(' '))

m = [list(map(int,input().strip())) for _ in range(2)]
visit = [[0]*n for _ in range(2)]
def bfs(x,y,c):
    q=deque()
    q.append((x,y,c))
    
    while q:
        x,y,c = q.popleft()

        if x==0:
            nx = x+1
            ny = y+k
            if n<=ny:
                print(1)
                return
            else:
                if m[nx][ny]==1 and ny>c and visit[nx][ny]!=1:
                    visit[nx][ny]=1
                    q.append((nx,ny,c+1))

        else:
            nx = x-1
            ny = y+k
            if n<=ny:
                print(1)
                return
            else:
                if m[nx][ny]==1 and ny>c and visit[nx][ny]!=1:
                    visit[nx][ny]=1
                    q.append((nx,ny,c+1))

        nx = x
        ny = y+1
        if n<=ny:
            print(1)
            return
        else:
            if m[nx][ny]==1 and ny>c and visit[nx][ny]!=1:
                visit[nx][ny]=1
                q.append((nx,ny,c+1))
        nx = x
        ny = y-1
        if n<=ny:
            print(1)
            return
        else:
            if m[nx][ny]==1 and ny>c and visit[nx][ny]!=1:
                visit[nx][ny]=1
                q.append((nx,ny,c+1))



    print(0)
    return

bfs(0,0,0)