n = int(input())
tri=[]
for i in range(n):
    line = list(map(int,input().split(' ')))
    tri.append(line)
result=[[] for _ in range(n)]
result[0]=tri[0][0]
if n==1:
    print(result[0])
else:
    result[1].append(result[0]+tri[1][0])
    result[1].append(result[0]+tri[1][1])
    for i in range(2, n):
        result[i].append(result[i-1][0]+tri[i][0])
        for j in range(1,i):
            result[i].append(max(result[i-1][j-1]+tri[i][j], result[i-1][j]+tri[i][j]))
        result[i].append(result[i-1][i-1]+tri[i][i])
    print(max(result[n-1]))
