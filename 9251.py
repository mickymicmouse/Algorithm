string=[]
for i in range(2):
    word = list(map(str, input()))
    string.append(word)
x=len(string[0])
y=len(string[1])
dp = [[0]*(y+1)for _ in range(x+1)]
for i in range(1,x+1):
    for j in range(1,y+1):
        if string[0][i-1]==string[1][j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])
print(dp[x][y])
