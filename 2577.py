a=int(input())
b=int(input())
c=int(input())

d = a*b*c
e = list(str(d))
for i in range(0,10,1):
    print(e.count(str(i)))