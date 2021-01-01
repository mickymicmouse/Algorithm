n,k=map(int, input().split(' '))
dp = [[0]*(k+1) for _ in range(n+1)]
coin = [int(input()) for _ in range(n)]
coin.sort()
for h in range(1,n+1): #3
    for w in range(k+1): #10
        if h==1 and w%coin[h-1]==0:
            dp[h][w]=1
        if w==0:
            dp[h][w]=1
        else:
            if w//coin[h-1]==0:
                dp[h][w]=dp[h-1][w]
            else:
                dp[h][w]=dp[h][w-coin[h-1]]+dp[h-1][w]
print(dp[n][k])
#메모리 문제가 발생하게됨, 아마 2차원 배열을 사용해서 그런듯