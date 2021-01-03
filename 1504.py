import sys
from heapq import heappush,heappop
input=sys.stdin.readline
N,E = list(map(int,input().split(' ')))
adj=dict()
for i in range(1, N+1):
    adj[i]=[]
for i in range(E):
    a,b,w = list(map(int,input().split(' ')))
    adj[a].append((b,w))
    adj[b].append((a,w))
v1,v2 = list(map(int,input().split(' ')))
start=1
INF = float('inf')

def dijkstra(start):
    visited=[INF]*(N+1)
    q = []
    heappush(q,(0,start))
    visited[start]=0
    while q:
        dist, node = heappop(q)
        for n_node,n_dist in adj[node]:
            if visited[node]+n_dist < visited[n_node]:
                visited[n_node] = visited[node]+n_dist
                heappush(q,(n_dist,n_node))
    return visited

result1 = dijkstra(start)
result2 = dijkstra(v1)
result3 = dijkstra(v2)
result = min(result1[v1]+result2[v2]+result3[N], result1[v2]+ result3[v1]+result2[N])
if result==INF:
    print(-1)
else:
    print(result)


#이렇게 할필요없이 함수에 시작수만 전달해줘서 start, v1, v2만 돌리면 갈수있는 최소경로는 visited에서 찾을수 있다.!


