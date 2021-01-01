n = int(input())
# 앞으로 한번 뒤로 한번 for문을 돌려서 프린트해주면 됨.
# 다음 것이 크고 그때까지의 최대값을 현재 dp에 넣어주고 +1
# 아닐 경우 0에서 +1
A=list(map(int,input().split(' ')))
max_index = A.index(max(A))
front=[0 for i in range(n)]
back = [0 for i in range(n)]
result = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if A[i]>A[j] and front[i]<front[j]:
            front[i]=front[j]
    front[i]+=1
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if A[i]>A[j] and back[i]<back[j]:
            back[i]=back[j]
    back[i]+=1
for i in range(n):
    result[i]=front[i]+back[i]-1

print(max(result))

