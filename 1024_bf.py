import sys
input = sys.stdin.readline
n,l = map(int,input().split(' '))
cnt=1
c_n=n
c_l=l
flag=False
start=0
d=0

while True:
    if flag==True or c_l>100:
        break

    for i in range(1, n//c_l+2):
        num=0
        for j in range(i, i+c_l):
            num+=j
        if num==n:
            flag=True
            start=i
            d = c_l

            break
    c_l+=1

if flag==False:
    print(-1)
else:
    for i in range(start, start+d):
        print(i, end=' ')



