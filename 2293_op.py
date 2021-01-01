n,k=map(int, input().split(' '))
dp = [0]*(k+1)
coin = [int(input()) for _ in range(n)]
coin.sort()
dp[0]=1
for i in coin:
    for j in range(i, k+1):
        dp[j]+=dp[j-i]
print(dp[k])