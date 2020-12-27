T = int(input())
for i in range(T):
    k=int(input()) #floor
    n=int(input()) #ho
    apart = [[0]*n for _ in range(k+1)]
    for s in range(k+1):
        for j in range(n):
            if j==0:
                apart[s][j]=1
                continue
            if s==0:
                apart[s][j]=j+1
                continue
            apart[s][j]=apart[s-1][j]+apart[s][j-1]
    print(apart[k][n-1])