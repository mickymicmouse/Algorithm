n,l = map(int,input().split(' '))
t=0
x=-1
d = 0

for i in range(l, 101):
    t = ((i**2)-i)/2
    if (n-t)%i==0 and (n-t)//i>=0:
        x=(n-t)//i
        d=i
        break

if x==-1:
    print(-1)
else:
    for i in range(int(x),int(x+d)): print(i, end=' ')