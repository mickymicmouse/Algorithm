n,m = list(map(int,input().split(' ')))
visited=[0]*(n+1)
result=[0]*m
def make(index):
    if index == m :
        print(*result)
        return
    for i in range(1,n+1):
        result[index]=i
        make(index+1)

make(0)
        