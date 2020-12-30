N = int(input())
A=[list(map(int,input().split(' '))) for _ in range(N)]
A = sorted(A, key = lambda x : (x[1],x[0]))
#끝나는 시간에 따라 회의 개수가 영향을 받으므로 
#회의 끝나는 시간 우선 정렬 후 끝나는 시간이 동일할 경우 
# 빨리 시작되는 순서대로 정렬해야함

schedule = []
count=1
end = A[0][1]
for i in range(1, N):
    if A[i][0]>=end:
        count+=1
        end = A[i][1]
print(count)