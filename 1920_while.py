import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
n_list = list(map(int,input().split(' ')))
m = int(input())
m_list = list(map(int,input().split(' ')))
n_list.sort()

for i in m_list:
    low = 0
    high = len(n_list)
    temp=False
    while low<high:
        mid = (low+high)//2
        if i>n_list[mid]:
            low = mid+1
        elif i<n_list[mid]:
            high=mid-1
        else:
            temp=True
            break

    if temp:
        print(1)
    else:
        print(0)


