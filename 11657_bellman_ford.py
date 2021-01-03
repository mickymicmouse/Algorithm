import sys
#음수가 존재한다면 벨만포드 알고리즘을 사용하여야 한다.
# 벨만포드는 힙큐를 사용하는 것이아닌 리스트를 사용하여 반복적으로 돌려주는 것
# O(VE) 의 시간 복잡도 다익스트라는 O(E log E)
input=sys.stdin.readline
N,M = list(map(int,input().split(' ')))
adj=dict()
for i in range(1,N+1):
    adj[i]=list()
for i in range(M):
    a,b,c = list(map(int,input().split(' ')))
    adj[a].append((b,c))
INF=float('inf')

def bellman_ford():
    possible=True
    visited=[INF]*(N+1)
    visited[1]=0
    for i in range(N):
        for j in range(1,N+1):
            for n_node, n_dist in adj[j]:
                if visited[j]!=INF and visited[j]+n_dist<visited[n_node]:
                    visited[n_node] = visited[j]+n_dist
                    if i==N-1:
                        possible=False
    return visited, possible

result,isPossible=bellman_ford()
if isPossible==False:
    print(-1)
else:
    for i in result[2:]:
        if i==INF:
            print(-1)
        else:
            print(i)
