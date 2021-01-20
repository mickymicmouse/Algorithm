from collections import deque
t = int(input())

def check(l, val):
    for s in range(1, len(l)):
        if l[s]>val:
            return False
    return True


for i in range(t):
    count=1
    n,m = map(int,input().split(' '))
    d = list(map(int,input().split(' ')))
    q=deque()
    for s in d: q.append(s)
    index = deque()
    for s in range(len(q)): index.append(s)
    while q:
        isHigh = check(q, q[0])
        if isHigh:
            if index[0]==m:
                print(count)
                break
            else:
                q.popleft()
                count+=1
                index.popleft()
        else:
            f = q.popleft()
            q.append(f)
            f = index.popleft()
            index.append(f)
    
            

