from collections import deque
n, k = map(int,input().split(' '))
q=deque()
result=[]
for i in range(1,n+1): q.append(i)

print('<', end='')
while q:
    for i in range(k-1):
        val = q.popleft()
        q.append(val)
    print(q.popleft(), end='')
    if q:
        print(', ',end='')
print('>')


