import sys
t = int(input())

for i in range(t):
    k=[]
    n = int(input())
    result=True
    for j in range(n):
        k.append(sys.stdin.readline().strip())
    k.sort(key=len)
    for s in range(len(k)):
        for h in range(s+1, len(k)):
            if k[s]==k[h][0:len(k[s])]:
                result=False
                break
        if result==False:
            break
    if result==False:
        print('NO')
    else:
        print('YES')
            


