N = int(input())
line = [int(input()) for _ in range(N)]
line.sort()
for i in range(N):
    print(line[i])