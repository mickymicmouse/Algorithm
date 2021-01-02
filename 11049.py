#11066에서 한 대각선 DP를사용해서 행렬의 곱셈 문제를 풀수 있다.
n = int(input())
shape= []
for i in range(n):
    x,y = list(map(int,input().split(' ')))
    shape.append((x,y))
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(2,n+1): #각 대각선으로 도는 부분
    for x in range(1, n-i+2): #대각선 위에서 도는 부분
        y=x+i-1
        minimum=[matrix[x][x+s]+matrix[x+s+1][y]+(shape[x-1][0]*shape[x+s-1][1]*shape[y-1][1]) for s in range(y-x)]
        matrix[x][y]=min(minimum)
print(matrix[1][n])

