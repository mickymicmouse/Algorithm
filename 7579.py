import sys
input = sys.stdin.readline
N,M = list(map(int,input().split(' ')))
me = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))
""" mc = list(zip(me,c))
mc.sort(key=lambda x: x[0])
mc.sort(key=lambda x: x[1])
# 같은수일 경우를 먼저 정렬
# 이후 원하는 키워드를 넣어서 정렬 """

dp = [[0]*(sum(c)+1) for _ in range(N+1)]
result=sum(c)
for i in range(1,N+1):
    for j in range(1, sum(c)+1):
        if c[i-1]<=j:
            dp[i][j]=max(me[i-1]+dp[i-1][j-c[i-1]], dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
        if dp[i][j]>=M:
            result = min(result,j)

if M!=0:
    print(result)
else:
    print(0)


    




