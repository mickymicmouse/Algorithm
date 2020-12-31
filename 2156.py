n=int(input())
# 이번단계의 포도주를 먹지 않는 것, 
# 이번 단계의 포도주를 먹고 전단계의 포도주를 먹고 전전단계의 포도주를 먹지 않는 것,
# 이번 단계의 포도주를 먹고 전단계의 포도주를 먹지 않는 것의 단계로 구분하여 각 횟수의 최대값을 구함  
# 경우의 수 문제같은 경우에는 각 전단계의 경우를 계산하여 더해주는 식으로 풀어줌
amount=[0]
for i in range(n):
    amount.append(int(input()))
dp = [0]*(n+1)
dp[1]=amount[1]
if n>1:
    dp[2]=amount[1]+amount[2]
for i in range(3,n+1):
    dp[i]=max(dp[i-1], dp[i-2]+amount[i], dp[i-3]+amount[i-1]+amount[i])
print(dp[n])
