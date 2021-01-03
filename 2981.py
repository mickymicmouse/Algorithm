N=int(input())
nums = [int(input()) for _ in range(N)]
# 뺀 수들의 최소 공약수의 약수 리스트가 답이 된다.
# (6,34,38)-> (28,4)의 최소 공약수인 4의 약수 리스트
import math
for i in range(1,N):
    if i==1:
        max_divisor=abs(nums[1]-nums[0])
    max_divisor = math.gcd(max_divisor, abs(nums[i]-nums[i-1]))

divisors=[max_divisor]
for i in range(2, int(max_divisor**0.5)+1):
    if max_divisor%i==0:
        divisors.append(i)
        if max_divisor//i!=i:
            divisors.append(max_divisor//i)
divisors.sort()
print(*divisors)
    