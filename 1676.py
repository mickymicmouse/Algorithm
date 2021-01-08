n=int(input())
dp = [1]*(n+1)
for i in range(1,n+1):
    dp[i]=dp[i-1]*i
num=str(dp[n])
result=0

for i in range(len(num)-1,-1,-1):
    if num[i]=='0':
        result+=1
    else:
        break
print(result)


