import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split(' '))
p = list(map(int,input().split(' ')))
q=deque()
count = 0
l = [i for i in range(1,n+1)]

def left(x):
    global count
    while True:
        if l[0]==x:
            break
        val = l.pop(0)
        l.append(val)
        count+=1

def right(x):
    global count
    while True:
        if l[0]==x:
            break
        val = l.pop()
        l.insert(0, val)
        count+=1

for i in p:
    idx = l.index(i)
    if idx <= len(l)//2:
        left(i)
    else:
        right(i)
    l.pop(0)
print(count)
    


