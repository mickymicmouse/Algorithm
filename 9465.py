t = int(input())

dx = [1,1,2,2]
dy = [1,-1,1,-1]

def bfs(x,y):
    result=0
    q = list()
    q.append((x,y))
    dp=[[0]*n for _ in range(2)]
    dp[y][x]=st[y][x]
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<2:
                if dp[ny][nx]<=dp[y][x]+st[ny][nx]:
                    q.append((nx,ny))
                    dp[ny][nx]=dp[y][x]+st[ny][nx]
                    result=max(result, dp[ny][nx])
    print(dp)
    return result

for _ in range(t):
    result=0
    n = int(input())
    st = []
    for i in range(2):
        st.append(list(map(int,input().split(' '))))
    for i in range(2):
        for j in range(2):
            result = max(bfs(i,j),result)
    print(result)