import math
dp = [1]*(1000001)
for i in range(1, 1000001):
    x=math.floor(i-math.sqrt(i))
    y=math.floor(math.log(i))
    z=math.floor(i*math.pow(math.sin(i),2))

    dp[i]=dp[x]+dp[y]+dp[z]




while True:
    i=int(input())
    if i==-1:
        break
    print(dp[i]%1000000)
    