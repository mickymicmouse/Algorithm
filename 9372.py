from collections import deque

def bfs(start):
    visited[s]=1
    queue=deque()
    queue.append(start)
    cnt=0
    while queue:
        for k in dic[queue.popleft()]:
            if visited[k]==0:
                visited[k]=1
                cnt+=1
                queue.append(k)
    return cnt


T = int(input())
for i in range(T):
    N, M = list(map(int,input().split(' ')))
    # N = 국가의 수, M = 비행기의 종류
    dic = dict()
    for s in range(1, N+1):
        dic[s]=set()
    for j in range(M):
        a,b = list(map(int,input().split(' ')))
        dic[a].add(b)
        dic[b].add(a)
    visited=[0 for _ in range(N+1)]
    count=0
    for s in dic:
        
        if visited[s]==0:
            route = bfs(s)
            count+=route
    print(count)
    
    
