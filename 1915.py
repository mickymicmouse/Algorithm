n,m = list(map(int,input().split(' ')))
square = []
dp = [[0]*m for _ in range(n)]
for i in range(n):
    square.append(list(map(int,input())))

result = 0
for i in range(n):
    for j in range(m):
        if square[i][j]==1 and (i==0 or j==0):
            dp[i][j]=1
            result=1


for i in range(1, n):
    for j in range(1,m):
        if square[i][j]==1:
            dp[i][j]=min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        result = max(dp[i][j],result)
print(result**2)