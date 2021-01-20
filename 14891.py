wheel=[]
for i in range(4):
    a=list(input())
    wheel.append(a)
k=int(input())

def turning(n, d):
    if dp[n]==1:
        return
    dp[n]=1
    if n==0:
        if wheel[n][2]!=wheel[n+1][6]:
            s = d*(-1)
            turning(n+1,s)
    elif n==3:
        if wheel[n][6]!=wheel[n-1][2]:
            s= d*(-1)
            turning(n-1,s)
    else:
        if wheel[n][6]!=wheel[n-1][2]:
            s=d*(-1)
            turning(n-1,s)
        if wheel[n][2]!=wheel[n+1][6]:
            s = d*(-1)
            turning(n+1,s)

    if d==-1:        
        temp = wheel[n].pop(0)
        wheel[n].append(temp)
    else:
        temp = wheel[n].pop()
        wheel[n].insert(0,temp)
    return
    

def score():
    result=0
    for f in range(4):
        if wheel[f][0]=='1':
            val = 2**f
            result+=val
    return result

for i in range(k):
    n,d = list(map(int,input().split(' ')))
    dp = [-1]*4
    turning(n-1,d)
print(score())
