from collections import deque
T = int(input())
dx = [-1,0,1]

def bfs():
    
    
    while queue:
        x,k = queue.pop(0)
        for j in range(3):
            nx = x+k+dx[j]
            if x<=nx<=y and line[nx]==0:
                    line[nx]=line[x]+1
                    queue.append((nx, k+dx[j]))

for i in range(T):
    x,y = map(int,input().split(' '))
    line = [0]*(y+1)
    queue=[]
    queue.append((x, 0))
    bfs()
    print(line[y-1])
    print(line)


