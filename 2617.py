import sys
input=sys.stdin.readline
from collections import deque
nop = set()
n,m = list(map(int, input().split(' ')))


hball = dict()
lball = dict()
for i in range(1, n+1):
    hball[i]=[]
    lball[i]=[]
for _ in range(m):
    h, l = map(int,input().split(' '))
    hball[h].append(l)
    lball[l].append(h)


for i in range(1,n+1):
    q = deque()
    q.append((i, 1))
    while q:
        print(q)
        b, num = q.popleft()
        if num>=(n+1)//2:
            nop.add(b)
            break
        for k in hball[b]:
            q.append((k,num+1))

for i in range(1,n+1):
    q = deque()
    q.append((i, 1))
    while q:
        print(q)
        b, num = q.popleft()
        if num>=(n+1)//2:
            nop.add(b)
            break
        for k in lball[b]:
            q.append((k,num+1))
print(nop)
print(len(nop))



