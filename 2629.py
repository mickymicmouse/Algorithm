import sys
input = sys.stdin.readline
n = int(input())
c = list(map(int,input().split(' ')))
t = int(input())
w = list(map(int,input().split(' ')))

dp = [[0]*(max(w)+1) for _ in range(n+1)]

for i in range(1, n+1): # 추의 종류 1~n
    for j in range(1, max(w)+1): #구슬의 무게 1~max(w)
        if dp[i-1][j]==1: # 위의 추로도 평가 가능할 경우
            dp[i][j]=1
        else: # 안될 경우
            if c[i-1]==j: # 추랑 구슬의 무게가 동일한 경우
                dp[i][j]=1
            else: # 동일 하지 않을 경우
                if dp[i-1][abs(c[i-1]-j)]==1:
                    dp[i][j]=1

# for i in dp: print(i) 
for i in range(t):
    if i==t-1:
        if dp[n][w[i]]==1:
            print('Y')
        else:
            print('N')
    else:
        if dp[n][w[i]]==1:
            print('Y',end=' ')
        else:
            print('N',end=' ')



