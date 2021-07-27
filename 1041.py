import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split(' ')))
idx = [i for i in range(6)]
ju =list(zip(idx, num))
ju.sort(key = lambda x: x[1])
match = dict()
for i in range(6):
    match[i]=5-i

from itertools import combinations as C
def point():
    c = 4
    
    x = list(C(ju,3))
    val = float('inf')
    for x1,x2,x3 in x:
        if match[x1[0]]!=x2[0] and match[x2[0]]!=x3[0] and match[x1[0]]!=x3[0]:
            val = min(val, x1[1]+x2[1]+x3[1])

    return val*c

def edge():
    if n==2:
        c = 4
    else:
        c = 8*(n-2)+4
    x = list(C(ju,2))
    val = float('inf')
    for x1,x2 in x:
        if match[x1[0]]!=x2[0]:

            val = min(val, x1[1]+x2[1])

    return val*c

def plane():
    if n==2:
        return 0
    else:
        c=5*((n-2)**2)+(n-2)*4    
    return min(num)*c


if n==1:
    print(sum(num)-max(num))
else:
    print(plane()+edge()+point())

