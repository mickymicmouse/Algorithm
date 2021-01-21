import sys
input = sys.stdin.readline
from collections import deque


dx = [0,0,-1,1]
dy = [1,-1,0,0]


for t in range(int(input())):
    n = int(input())
    p = [list(map(int,input().split(' '))) for _ in range(n+2)]
    d = [[float('inf')]*(n+2) for _ in range(n+2)]

    for i in range(n+2):
        for j in range(n+2):
            if i==j:
                continue
            
            di = abs(p[i][0]-p[j][0])+abs(p[i][1]-p[j][1])
            if di<=1000:
                d[i][j]=1
    
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if d[i][j]>d[i][k]+d[k][j]:
                    d[i][j]=d[i][k]+d[k][j]

    if 0<=d[0][n+1]<float('inf'):
        print('happy')
    else:
        print('sad')
    print(d)    

    


