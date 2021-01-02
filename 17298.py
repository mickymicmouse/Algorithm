import sys
input= sys.stdin.readline
n = int(input())
A = list(map(int,input().split(' ')))
result=[-1 for _ in range(n)]
stack=[]
for i in range(n):
    while len(stack)!=0 and A[stack[-1]]<A[i]:
        result[stack.pop()]=A[i]
    stack.append(i)
print(*result)