import sys
input = sys.stdin.readline
from collections import deque
import math
t = int(input())


def d(x):
    if x ==0:
        return 0
    else:
        return (2*x) % 10000

def s(x):
    if x==0:
        val = 9999
    else:
        val=x-1
    return val

def l(x):
    if x==0:
        return 0
    ss = 3
    if ss==0:
        val=x
    else:
        front = x//(10**ss)
        back = x%(10**ss)
        val = back*10+front
    return val

def r(x):
    if x==0:
        return 0
    ss=3
    if ss==0:
        val=x
    else:
        front = int(x//10)
        back = int(x%10)
        val = back*(10**ss)+front
    return val

def bfs(x):
    dp = [0]*10001
    q=deque()
    q.append(x)
    dp[x]=''
    while q:
        x = q.popleft()
        if x==b:
            return dp[x]
        nx = d(x)
        if dp[nx]==0:
            dp[nx]=dp[x]+'D'
            q.append(nx)
        nx = s(x)
        if dp[nx]==0:
            dp[nx]=dp[x]+'S'
            q.append(nx)
        nx = l(x)
        if dp[nx]==0:
            dp[nx]=dp[x]+'L'
            q.append(nx)
        nx = r(x)
        if dp[nx]==0:
            dp[nx]=dp[x]+'R'
            q.append(nx)
    return


for _ in range(t):
    a,b = map(int,input().split(' '))
    print(bfs(a))