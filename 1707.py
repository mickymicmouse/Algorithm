import sys
input=sys.stdin.readline
from collections import deque

# 떨어져 있는 즉, 연결되어 있지 않는 노드까지 판단하기 위해 V개를 for문 돌려주는 것
# bfs에서는 인접한 노드가 같은지만 판단해주면 된다.
# +,-로 구분해주면 된다.

t = int(input())

def bfs(start):
    queue=deque()
    queue.append(start)
    dp[start]=1
    while queue:
        x = queue.popleft()
        for nx in adj[x]:
            if dp[nx]==0:
                dp[nx]=-dp[x]
                queue.append(nx)
            else:
                if dp[nx]==dp[x]:
                    return False
    return True


for i in range(t):
    V,E = list(map(int,input().split(' ')))
    adj=dict()
    isTrue = True
    dp = [0]*(V+1)
    for j in range(1,V+1):
        adj[j]=list()
    for j in range(E):
        a,b=list(map(int,input().split(' ')))
        adj[a].append(b)
        adj[b].append(a)
    for j in range(1,V+1):
        if dp[j]==0:
            result=bfs(j)
            if result==False:
                isTrue=False
                break
    if isTrue:
        print('YES')
    else:
        print('NO')

    

