n, k = map(int,input().split(' '))
ob = []
dp = [[0]*(k+1) for _ in range(n+1)]

# 무게별 가치를 측정하는 매트릭스를 만들어라
# 즉, 새로 들어온 물체 이전까지의 최고 가치와 새로들어온 물체의 무게를 제외한 최고가치 + 현재 물체의 가치 중 높은 가치를
# 현재 최대 가치로 넣어주는 DP 메트릭을 구성하는 것이다.

for i in range(n):
    w,v = map(int,input().split(' '))
    ob.append([w,v])

for i in range(1,n+1):
    for j in range(k,0,-1):
        if j-ob[i-1][0]>=0:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-ob[i-1][0]]+ob[i-1][1])
        else:
            dp[i][j]=dp[i-1][j]
print(max(dp[n]))