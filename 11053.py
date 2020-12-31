n=int(input())
# 이전 숫자들에서 자신보다 작은 숫자들 중 가장 큰 길이 +1이 현재 최대 길이가 되는 것
A = list(map(int, input().split(' ')))
dp=[0]*n
for i in range(n):
    for j in range(i):
        if A[i]>A[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))