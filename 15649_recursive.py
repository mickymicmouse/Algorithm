n,m = list(map(int,input().split(' ')))

visited=[0]*(n+1)
result = [0]*m
x=[]
def make(index):
    if index == m:
        print(*result)
        return
    for i in range(1,n+1):
        if visited[i]==1:
            continue
        visited[i]=1
        result[index]=i
        make(index+1)
        visited[i]=0

make(0)
