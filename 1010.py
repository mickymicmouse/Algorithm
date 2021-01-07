#서쪽은 k, 동쪽은 n이 되는 nCk를 구하면 됨
T = int(input())
dp = [[1]*30 for _ in range(30)]
for i in range(2,30):
    for j in range(1,i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

for i in range(T):
    k,n = list(map(int,input().split(' ')))
    print(dp[n][k])