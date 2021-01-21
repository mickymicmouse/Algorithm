import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
d = [[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split(' '))
    d[a][b]=min(c, d[a][b])

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                d[i][j]=0
            else:
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

for i in d[1:]:
    for j in i[1:]:
        if j == float('inf'):
            print(0, end=" ")
        else:
            print(j, end=" ")
    print()