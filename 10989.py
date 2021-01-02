import sys
input=sys.stdin.readline
n = int(input())
line = [0]*10001
for i in range(n):
    line[int(input())]+=1
for i in range(10001):
    if line[i]>0:
        for j in range(line[i]):
            print(i)
