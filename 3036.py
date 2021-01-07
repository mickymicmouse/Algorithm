import math
n = int(input())
wheel = list(map(int,input().split(' ')))
start = wheel[0]
for i in wheel[1:]:
    divisor = math.gcd(2*start, 2*i)
    x = (2*start)//divisor
    y = (2*i)//divisor
    print("%d/%d"%(x,y))