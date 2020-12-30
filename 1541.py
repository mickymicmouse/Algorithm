equ = input().split('-')
nums = []
for i in equ:
    line = i.split('+')
    cnt=0
    for j in line:
        cnt+=int(j)
    nums.append(cnt)
start = nums[0]    
for i in range(1, len(nums)):
    start-=nums[i]
print(start)
# eval함수는 시작하는 수가 0일 경우 
# runtime error를 발생시키기 때문에 사용할 수 없다.