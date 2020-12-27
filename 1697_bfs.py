from collections import deque

dx = [1,-1]

def bfs():
    while queue:
        x = queue.popleft()
        
        for i in range(3):
            if i <=1:
                nx = dx[i]+x
            if i ==2:
                nx = 2*x
            
            if 0<=nx<100001 and line[nx]==0:
                queue.append(nx)
                line[nx]=line[x]+1
            if 0<=nx<100001 and line[nx]!=0 and line[x]+1<line[nx]:
                queue.append(nx)
                line[nx]=line[x]+1

                

N, K = list(map(int, input().split(' ')))
line = [0]*100002
queue = deque()
queue.append(N)
line[N]=1

bfs()
print(line[K]-1)

