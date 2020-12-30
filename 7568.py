# 각 라인의 학생의 등수 즉, 자기보다 큰사람만 세서 프린트하면 되는구나!

N = int(input())
line = []
for i in range(N):
    x,y = map(int, input().split(' '))
    line.append((x,y))

for i in range(N):
    rank=1
    for j in range(N):
        if line[i][0]<line[j][0] and line[i][1] < line[j][1]:
            rank+=1
    print(rank, end=' ')