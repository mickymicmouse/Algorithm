n = int(input())
road = []
for i in range(n):
    road.append(list(input().split(' ')))


dx = [1,0]
dy = [0,1]

def minBfs():
    dp = [[float('inf')]*(n) for _ in range(n)]
    q=[]
    q.append((0,0))
    dp[0][0]=road[0][0]
    while q:
        x,y = q.pop(0)
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<n and ny<n:
                if road[nx][ny]=='*' or road[nx][ny]=='+' or road[nx][ny]=='-':
                    dp[nx][ny]=min(int(dp[x][y]), dp[nx][ny])
                    q.append((nx,ny))
                else:
                    dp[nx][ny]=min(eval(str(dp[x][y])+road[x][y]+road[nx][ny]),dp[nx][ny])
                    q.append((nx,ny))
    return dp[n-1][n-1]

def maxBfs():
    dp = [[-float('inf')]*(n) for _ in range(n)]
    q=[]
    q.append((0,0))
    dp[0][0]=road[0][0]
    while q:
        x,y = q.pop(0)
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<n and ny<n:
                if road[nx][ny]=='*' or road[nx][ny]=='+' or road[nx][ny]=='-':
                    dp[nx][ny]=max(int(dp[x][y]), dp[nx][ny])
                    q.append((nx,ny))
                else:
                    dp[nx][ny]=max(eval(str(dp[x][y])+road[x][y]+road[nx][ny]),dp[nx][ny])
                    q.append((nx,ny))
    return dp[n-1][n-1]

a=maxBfs()
b=minBfs()
print(a,b)

                    