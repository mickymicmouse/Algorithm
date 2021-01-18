n,m = list(map(int,input().split(' ')))

visited=[0]*(n+1)
result = [0]*m
x=[]
def make(index,start_num):
    if index == m:
        print(*result)
        return
    for i in range(start_num,n+1):
        if visited[i]==1:
            continue
        visited[i]=1
        result[index]=i
        make(index+1, i)
        visited[i]=0

make(0, 1)