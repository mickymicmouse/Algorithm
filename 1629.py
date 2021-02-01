import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
a,b,c = map(int,input().split(' '))

seq = []
while True:
    if b==1:
        break
    if b%2==0:
        seq.append(0)
    else:
        seq.append(1)
    b=b//2

result = a%c
for i in seq[::-1]:
    if i==1:
        result=result**2 * (a%c)
    else:
        result = result**2
    result=result%c
print(result)