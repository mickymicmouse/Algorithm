N = int(input())
P = list(map(int, input().split(' ')))
P = sorted(P)
time = []
for i in range(N):
    time.append(sum(P[0:i+1]))
print(time)
print(sum(time))