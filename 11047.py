N, K = map(int, input().split(' '))
A=[int(input()) for _ in range(N)]
num=0
for i in range(N-1,-1,-1):
    if K==0:
        break
    if A[i]>K:
        continue
    num+=K//A[i]
    K %= A[i]
print(num)
