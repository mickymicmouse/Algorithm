n = int(input())
line=[]
for i in range(n):
    x,y = list(map(int,input().split(' ')))
    line.append((x,y))
line = sorted(line, key = lambda x : x[0])

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if line[i][1]>line[j][1] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(n-max(dp))

