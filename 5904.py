n = int(input())

dp = [3]

cnt=0
while True:
    value = 2*dp[cnt]+(cnt+3)+1
    dp.append(value)
    cnt+=1
    
    if value>n:
        s = dp.index(value)
        break

def find(s, n):
    if s==0:
        if n==1:
            return 'm'
        else:
            return 'o'
    if n<=dp[s-1]:
        return find(s-1, n)
    elif n>dp[s-1]+1+s+2:
        return find(s-1, n-(dp[s-1]+1+s+2))
    else:
        if n-dp[s-1]==1:
            return 'm'
        else:
            return 'o'
print(dp)
print(find(s, n))

