from collections import deque

def bfs():
    queue=deque()



T = int(input())
for i in range(T):
    N, M = list(map(int,input().split(' ')))
    # N = 국가의 수, M = 비행기의 종류
    dic = dict()
    for s in range(1, N+1):
        dic[s]=set()
    for j in range(M):
        a,b = list(map(int,input().split(' ')))
        dic[a]=b
        dic[b]=a
    
