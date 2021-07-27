import sys
input = sys.stdin.readline
import copy

n,m = map(int,input().split(' '))
table = [list(map(int,input().strip())) for _ in range(n)]
k= int(input())
arr = [0]*n

if k%2==0:
    for i in range(n):
        cnt=table[i].count(0)
        if cnt%2==0 and cnt<=k:
            for j in range(n):
                if table[i]==table[j]:
                    arr[i]+=1