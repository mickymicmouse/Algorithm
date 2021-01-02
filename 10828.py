import sys
input=sys.stdin.readline
n=int(input())
stack=[]

def push(x):
    stack.append(x)

def pop():
    if len(stack)>0:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)
def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[-1])


for i in range(n):
    operation = list(map(str,input().strip().split(' ')))
    print(operation)
    if operation[0]=='push':
        push(int(operation[1]))
    if operation[0]=='top':
        top()
    if operation[0]=='size':
        size()
    if operation[0]=='empty':
        empty()
    if operation[0]=='pop':
        pop()
        
    