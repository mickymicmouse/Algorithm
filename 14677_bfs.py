import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
seq = list(map(str, input().strip()))
check = ['B','L','D']
t=3*n
dp = [[0]*1501 for _ in range(1501)]

def bfs():
    q=deque()
    q.append((0,0))
    dp[0][0]=1
    lv = -1
    time=0
    while q:
        size = len(q)
        while True:
            if size==0: break
            l,r =q.popleft()
            
            if l+r < t:
                if seq[l]==check[time] and dp[l+1][r]==0:
                    q.append((l+1,r))
                    dp[l+1][r]=1
                if seq[t-1-r]==check[time] and dp[l][r+1]==0:
                    q.append((l,r+1))
                    dp[l][r+1]=1
            size-=1
        lv+=1
        time= (time+1)%3
    return lv

result = bfs()
print(result)
