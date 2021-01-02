import sys
input=sys.stdin.readline
# 위의 코드는 시간 단축에 매우 중요!!!
N = int(input())
line = [0]+list(map(int,input().split(' ')))
q = int(input())

dp=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][i]=1

for i in range(N-1):
    for j in range(1, N-i):
        y = j+i+1
        if line[j]==line[y]:
            if y-j==1:
                dp[j][y]=1
            else:
                if dp[j+1][y-1]==1:
                    dp[j][y]=1
                

question = []
for i in range(q):
    x,y=list(map(int,input().split(' ')))
    print(dp[x][y])
