import sys
n=int(sys.stdin.readline().strip())
for i in range(n):
    r=sys.stdin.readline().strip()
    a,b=map(int,r.split(' '))
    print(a+b)