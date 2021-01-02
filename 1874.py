n=int(input())
nums = [int(input()) for _ in range(n)]
sort_nums=sorted(nums)
stack=[]
result=[]
signal=[]
cnt=0
while len(result)!=len(nums):
    if len(stack)==0:
        value=sort_nums.pop(0)
        stack.append(value)
        signal.append('+')
    elif stack[-1]!=nums[cnt]:
        if len(sort_nums)==0:
            print('NO')
            break
        else:
            value=sort_nums.pop(0)
            stack.append(value)
            signal.append('+')
    elif stack[-1]==nums[cnt]:
        value=stack.pop()
        cnt+=1
        result.append(value)
        signal.append('-')
if result==nums:
    for i in signal:
        print(i)
