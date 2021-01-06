
import sys
import collections
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
mean = round(sum(nums)/n)
print(mean)
mid = nums[n//2]
print(mid)
count = collections.Counter(nums)
c = [(i,j) for i,j in count.items()]

c.sort(key=lambda x : x[0])
c.sort(key=lambda x:x[1], reverse=True)
if n==1:
    print(nums[0])
else:
    if c[0][1]==c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
ran = max(nums)-min(nums)
print(ran)
