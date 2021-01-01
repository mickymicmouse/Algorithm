T = int(input())
# 각 자리까지의 최소합을 구해주어야함(DP로)
for i in range(T):
    n = int(input())
    page = list(map(int,input().split(' ')))
    dp = [[0]*(n+1) for i in range(n+1)]
    for x in range(1, n):
        y=x+1
        dp[x][y]=page[x-1]+page[x]
    # 대각선으로 진행되어야 하는구나!
    for f in range(n-2):
        for x in range(1, n-f-1):
            y = x+2+f
            minimum=[dp[x][x+s]+dp[x+s+1][y] for s in range(y-x)]
            dp[x][y]=min(minimum)+sum(page[x-1:y])
    print(dp[1][n])

    #pypy3으로 가능
    # 일단 dp는 각 자리까지의 최소합을 구해준다 
    #최소합의 경우 2차원 배열로 구성되어 있으며, 각 최소값은 그 자리까지의 합 + 전체 합이다
    # 즉 DP에 입력시에는 각 자리까지의 합의 최소를 구한 후 전체 합을 더해주면 된다.
    # (1,4) 를 구하는 경우 (1,1)(2,4)의 경우와 (1,2)(3,4) 의 경우, (1,3)(4,4) 의 경우가 존재한다.
    # 대각선으로 진행하여야하므로 값 입력시 대각선 진행이 가능하도록 짜야한다.
