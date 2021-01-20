from collections import deque
import sys
input = sys.stdin.readline
t= int(input())

def push_front(x):
    q.appendleft(x)
def push_back(x):
    q.append(x)
def pop_front():
    if q:
        print(q.popleft())
    else:
        print(-1)
def pop_back():
    if q:
        print(q.pop())
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
        print(q[0])
    else:
        print(-1)
def back():
    if q:
        print(q[-1])
    else:
        print(-1)

        
q=deque()
for i in range(t):
    d = input().strip().split(' ')
    
    if d[0]=='push_front':
        push_front(d[1])
    elif d[0]=='push_back':
        push_back(d[1])
    elif d[0]=='pop_front':
        pop_front()
    elif d[0]=='pop_back':
        pop_back()
    elif d[0]=='size':
        size()
    elif d[0]=='empty':
        empty()
    elif d[0]=='front':
        front()
    elif d[0]=='back':
        back()
