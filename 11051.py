n,k = list(map(int,input().split(' ')))
# 파스칼의 삼각형 - 이항계수(조합)의 값들을 삼각형으로 나타낸 것!!!
dp = [[1]*1001 for _ in range(1001)]
for i in range(2,1001):
    for j in range(1,i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
print(dp[n][k]%10007)
