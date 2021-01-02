import sys
sys.setrecursionlimit(10000)
input= sys.stdin.readline
M,N = list(map(int,input().split(' ')))
square=[]
for i in range(M):
    line = list(map(int, input().split(' ')))
    square.append(line)
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def dfs():
    stack=[]
    stack.append((0,0))
    global cnt
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<M and 0<=ny<N: 
                if square[nx][ny]<square[x][y]:
                    if nx==M-1 and ny==N-1:
                        cnt+=1
                    else:
                        stack.append((nx,ny))

cnt=0
dfs()
print(cnt)
                