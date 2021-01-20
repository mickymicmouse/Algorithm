from collections import deque
n = int(input())

def move():
    val = q.popleft()
    q.append(val)
    
q=deque()
for i in range(1,n+1):
    q.append(i)

while True:
    if len(q)==1:
        break
    q.popleft()
    if len(q)==1:
        break
    move()
print(q[0])
