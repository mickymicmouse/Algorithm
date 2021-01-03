from collections import deque
import sys
# 이거 맨날 까먹는데 잘생각해봐
# BFS에서는 동시에 진행해서 count가 1씩 증가하니까 굳이 다음칸에 있는 수가 최소인지 최대인지 판단할 필요가 없다는 것
# 그리고 보통 bfs에서 시간초과는 목적지에 도착했을때 리턴해주는 부분하나를 추가함으로써 해결 가능
# 초기 인접행렬의 값은 통일만 해주면 상관없음 0 or inf
input = sys.stdin.readline
t=int(input())
dx=[2,2,1,1,-1,-1,-2,-2]
dy=[1,-1,2,-2,2,-2,1,-1]
INF=float('inf')
def bfs(x,y,d_x,d_y):
    queue = deque()
    queue.append((x,y))
    square = [[INF]*I for _ in range(I)]
    square[x][y]=0
    while queue:
        x,y=queue.popleft()
        if x==d_x and y==d_y:
            print(square[d_x][d_y])
            return
        for s in range(8):
            nx = x+dx[s]
            ny = y+dy[s]
            if 0<=nx<I and 0<=ny<I and square[nx][ny]==INF:
                #if square[nx][ny]>square[x][y]+1: 이부분이 필요없다는 것
                square[nx][ny]=square[x][y]+1
                queue.append((nx,ny))



for i in range(t):
    I = int(input())
    x,y=list(map(int,input().split(' ')))
    d_x,d_y=list(map(int,input().split(' ')))
    bfs(x,y,d_x,d_y)
    
    