import datetime
start = datetime.datetime.now()
string = list(map(str, input().strip()))
n=len(string)
string = ['0']+string
s=str(string[1:])
dp = [[0]*(n+1) for _ in range(n+1)]
result = 0
d_x=0
d_y=0
ans=''
for f in range(n):
    for x in range(1, n-f+1):
        y=x+f
        if x==y:
            dp[x][y]=1
        elif dp[x+1][y-1]!=0 and string[x]==string[y] and y-x>=2:
            dp[x][y]=dp[x+1][y-1]+2
        elif string[x]==string[y] and y-x<2:
            dp[x][y]=2

        if result<=dp[x][y]:
            result=dp[x][y]
            d_x=x
            d_y=y
            
print(dp[d_x][d_y])
print(dp)
print(result)
print(d_x, d_y)
print(ans)
finish = datetime.datetime.now()
print(finish-start)

