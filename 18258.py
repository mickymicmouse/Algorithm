from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

def push(x):
    q.append(x)

def pop():
    if q:
        val = q.popleft()
        print(val)
    else:
        print(-1)
def size():
    print(len(q))
def empty():
    if q:
        print(0)
    else:
        print(1)
def front():
    if q:
        val = q[0]
        print(val)
    else:
        print(-1)
def back():
    if q:
        val = q[-1]
        print(val)
    else:
        print(-1)







q=deque()
for i in range(n):
    
    oper = input().strip().split(' ')
    if oper[0]=='push':
        push(oper[1])
    elif oper[0]=='pop':
        pop()
    elif oper[0]=='size':
        size()
    elif oper[0]=='empty':
        empty()
    elif oper[0]=='front':
        front()
    elif oper[0]=='back':
        back()

