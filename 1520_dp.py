
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
#sys.setrecursionlimit -> 재귀 횟수를 풀어주는 코드이다. 즉 재귀 반복작업을 하기 위해서는 위의 코드를 필수적으로 써주어야함
M,N = list(map(int,input().split(' ')))
square=[]
for i in range(M):
    line = list(map(int, input().split(' ')))
    square.append(line)
dp=[[-1]*N for _ in range(M)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# dfs와 dp의 혼합문제로써 심화된 방문상태를 dp에 저장하여야함
# dfs는 보통 재귀로 구현

def dfs(x,y):
    if x==M-1 and y==N-1:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<M and 0<=ny<N: 
                if square[nx][ny]<square[x][y]:
                    dp[x][y]+=dfs(nx,ny)
    
    return dp[x][y]
print(dfs(0,0))
