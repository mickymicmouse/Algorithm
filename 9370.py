import sys
from heapq import heappop, heappush
input=sys.stdin.readline
T = int(input())
INF=float('inf')
def dijkstra(start, n):
    q=[]
    visited=[INF]*(n+1)
    heappush(q, (0,start))
    visited[start]=0
    while q:
        dist, node = heappop(q)
        for n_node,n_dist in adj[node]:
            if visited[node]+n_dist<visited[n_node]:
                visited[n_node]=visited[node]+n_dist
                heappush(q,(visited[n_node],n_node))
    return visited

for s in range(T):
    n,m,t = list(map(int,input().split(' '))) # 교차로 도로 목적지
    s,g,h = list(map(int,input().split(' '))) # 출발지, 점선의 시작과 끝
    adj=dict()
    for i in range(1,n+1):
        adj[i]=list()
    for i in range(m):
        a,b,c=list(map(int,input().split(' ')))
        adj[a].append((b,c))
        adj[b].append((a,c))
    d = [int(input()) for _ in range(t)]
    result1 = dijkstra(s,n)
    result2 = dijkstra(g,n)
    result3 = dijkstra(h,n)
    goal=[]
    for i in d:
        min_route = min(result1[g]+result2[h]+result3[i], result1[h]+result3[g]+result2[i])
        if min_route!=INF and result1[i]>=min_route:
            goal.append(i)
    goal.sort()
    print(*goal)
        




