n,m=list(map(int,input().split(' ')))
result = [0]*m

def backtracking(index, start):
    if index==m:
        print(*result)
        return
    for i in range(start,n+1):
        result[index]=i
        backtracking(index+1, i)

backtracking(0,1)

