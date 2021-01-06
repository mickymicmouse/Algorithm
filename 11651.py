n = int(input())
nums = [list(map(int,input().split(' '))) for _ in range(n)]
nums.sort(key=lambda x:(x[1],x[0])) 
# 한줄에 쓰기 위해서는 위주가 되는 것이 앞에
# 두줄에 쓰기 위해서는 위주가 되는 것이 마지막에 오도록 설정
for i, j in nums:
    print(i,j)