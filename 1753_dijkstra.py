from heapq import heappush, heappop
import sys
input = sys.stdin.readline
#인접행렬이 아닌 인접 리스트 (딕트)를 사용하면 시간 초과가 일어나고
#이를 해결하기 위해서는 heap을 사용해야한다.
# heapq는 항상 최소값만을 리턴
#BFS구현이랑 동일하지만 heap을 사용한다는 것만 다름
V,E = list(map(int,input().split(' ')))
start = int(input())
graph = dict()
for i in range(1,V+1):
    graph[i]=[]
for i in range(E):
    u,v,w=list(map(int,input().split(' ')))
    graph[u].append([v,w])
INF = float('inf')
visited = [INF]*(V+1)

def dijkstra(start):
    queue=[]
    heappush(queue, (0,start))
    visited[start]=0
    while queue:
        cost, node=heappop(queue)
        for n_node,n_cost in graph[node]:
            if n_cost+visited[node] < visited[n_node]:
                visited[n_node]=n_cost+visited[node]
                heappush(queue,(visited[n_node], n_node))
dijkstra(start)
for i in range(1,V+1):
    if visited[i]!=INF:
        print(visited[i])
    else:
        print('INF')


    



