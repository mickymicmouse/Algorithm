import re
import sys

#정규표현식을 모르면 풀기 어려운 문제

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = str(input().strip())
    p=re.compile('(100+1+|01)+')
    m=p.fullmatch(s)
    if m:
        print('YES')
    else:
        print('NO')
