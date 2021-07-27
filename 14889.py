import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)
from itertools import combinations
n=int(input())
score = [list(map(int,input().split(' '))) for _ in range(n)]
select=[0]*n



def dfs(idx, cnt):
    global result
    if cnt==n//2:
        start, link = 0,0
        for i in range(n):
            for j in range(n):
                if select[i]==0 and select[j]==0:
                    start+=score[i][j]
                elif select[i]==1 and select[j]==1:
                    link+=score[i][j]
        result = min(result, abs(start-link))
    for i in range(idx, n):
        if select[i]==1:
            continue
        select[i]=1
        dfs(i+1, cnt + 1)
        select[i]=0
result = float('inf')
dfs(0, 0)

print(result)