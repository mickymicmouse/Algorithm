n=int(input())
cor = [list(map(int,input().split(' '))) for _ in range(n)]
cor.sort(key = lambda x : x[1])
cor.sort(key = lambda x : x[0])
for i,j in cor:
    print(i,j)
