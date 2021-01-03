import math

#최대공약수는 유클리드 호제법을 통해서 구함 gcd --> (24, 18) (18, 6) (6,0)
# (1071, 1029) (1029, 42) (42, 21) (21, 0)
a,b=list(map(int,input().split(' ')))
A=math.gcd(a,b)
if a>b:
    A=a
    B=b
else:
    A=b
    B=a
while B!=0:
    A=A%B
    A,B = B,A
print(A)
print(a*b/A)
