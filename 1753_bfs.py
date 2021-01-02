from collections import deque
import sys
input = sys.stdin.readline
V,E = list(map(int,input().split(' ')))
start = int(input())
graph = dict()
for i in range(V):
    graph[i+1]=[]

for i in range(E):
    u,v,w=list(map(int,input().split(' ')))
    graph[u].append((v,w))

visited = [10000000 for _ in range(V+1)]
def bfs(x):
    
    queue=deque()
    queue.append(x)
    while queue:
        value = queue.popleft()
        for i in graph[value]:
            if visited[value]==10000000:
                visited[i[0]]=i[1]
            else:
                visited[i[0]]=min(i[1]+visited[value],visited[i[0]])
            queue.append(i[0])

bfs(start)
for i in range(V):
    if i+1==start:
        print(0)
    else:
        if visited[i+1]==10000000:
            print('INF')
        else:
            print(visited[i+1])


    



