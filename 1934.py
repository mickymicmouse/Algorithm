import math
t=int(input())
for i in range(t):
    a,b = list(map(int,input().split(' ')))
    gc =math.gcd(a,b)
    print((a*b)//gc)

#유클리드 호제법의 힘!!!