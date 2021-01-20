import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    flag = True
    f = list(input().strip())
    n = int(input())
    if n==0:
        l = input()
        q = []
    else:
        q=list(map(int,input().strip()[1:-1].split(',')))
    direction=1
    flag = True
    first=0
    last=len(q)
    for s in f:
        if s=='R':
            direction*=(-1)
        elif s=='D':
            if first != last:
                if direction>0:
                    first+=1
                else:
                    last-=1
            else:
                print('error')
                flag = False
                break
    if flag:
        if direction==1:
            result = q[first:last]
        else:
            if first-1<0:
                result = q[last-1::-1]
            else:
                result = q[last-1:first-1:-1]
        result = str(result).replace(' ','')
        print(result)