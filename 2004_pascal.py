n,m = list(map(int,input().split(' ')))
dp=[[1]*(n+1) for _ in range(n+1)]
for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
num=str(dp[n][m])
result=0
for i in range(len(num)-1,-1,-1):
    if num[i]=='0':
        result+=1
    else:
        break
print(result)
#파스칼의 삼각형으로 했는데 메모리 에러
# 2,000,000,000이 최대 이므로