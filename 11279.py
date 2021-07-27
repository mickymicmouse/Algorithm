import sys
input = sys.stdin.readline

n = int(input())


def push(value):
    if len(array)==0:
        print(0)
    else:
        num = array.pop()
        print(num)
    
    

array = []
for i in range(n):
    k = int(input())
    if k==0:
        push(k)
    else:
        array.append(k)
        array.sort()