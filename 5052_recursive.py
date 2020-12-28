import sys
def check(nums, per):    
    for i in nums:
        if per>=len(test[i]):
            result.append('NO')
            return 0
        
    same = dict()
    for s in range(10):
        same[s]=set()
        for k in nums:
            if s==int(test[k][per]):
                same[s].add(k)
    for y in same.values():
        if len(y)>=2:
            nums = list(y)
            
            check(nums, per+1)
    result.append('YES')
    return 0
    

t = int(input())
for i in range(t):
    n = int(input())
    test = [sys.stdin.readline().strip() for _ in range(n)]
    test_index = [b for b in range(len(test))]
    result=[]
    check(test_index,0)
    
    if 'NO' in result:
        print('NO')
    else:
        print('YES')




    