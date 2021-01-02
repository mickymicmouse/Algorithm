import sys
input = sys.stdin.readline
k=int(input())
line = []
for i in range(k):
    value = int(input())
    if value==0:
        line.pop()
    else:
        line.append(value)

print(sum(line))