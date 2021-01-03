import sys
from heapq import heappush,heappop
#음수가 존재한다면 벨만포드 알고리즘을 사용하여야 한다.
input=sys.stdin.readline
N,M = list(map(int,input().split(' ')))

adj=dict()
for i in range(1,N+1):
    adj[i]=list()
for i in range(M):
    a,b,c = list(map(int,input().split(' ')))
    adj[a].append((b,c))
INF=float('inf')

def dijkstra(start):
    q=[]
    
    visited=[INF]*(N+1)
    heappush(q,(0,start))
    visited[start]=0
    cnt=0
    while q:
        if cnt>M+1000:
            return -1
        dist,node = heappop(q)
        for n_node,n_dist in adj[node]:
            if visited[node]+n_dist<visited[n_node]:
                visited[n_node]=visited[node]+n_dist
                heappush(q,(visited[n_node],n_node))
                cnt+=1
    return visited
result = dijkstra(1)
if result==-1:
    print(-1)
    exit()
else:
    for i in range(2,N+1):
        if result[i]==INF:
            print(-1)
        else:
            print(result[i])