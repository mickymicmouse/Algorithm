import math
def solution(n):
    answer = 0
    dp=[1]*(n+1)
    dp[0]=0
    dp[1]=0 # 0은 소수가 아님 1은 소수를 의미
    for i in range(int(math.sqrt(n))+1):
        cnt = 2
        while i<=n:
            i*=cnt
            dp[i]=0
            cnt+=1
    print(dp)
    

a=[1,2]
b=[3,4]
c=[5,6]
list(zip(a,b,c))
    
    return answer
solution(10)
import sys
sys.set

a=12
str(a)

a='12345'
from itertools import combinations as C
C(a,2)
for i in C(a,2):
    print(i)