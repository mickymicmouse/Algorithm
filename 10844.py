# 맨뒤에 올 경우의 수를 생각해서 자리수별 각 수가 올 경우의 수를 계산
# 이후 대각선 위의 합을 계산하면 그다음 자리수의 경우의 수가 나오게 됨
# 점화식을 활용하여 계산
N = int(input())
a=dict()
a[1]=[]
a[1]=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,N+1):
    a[i+1]=[]
    line=[]
    for j in range(10):
        if j==0:
            value = a[i][j+1]
        elif j==9:
            value = a[i][j-1]
        else:
            value = a[i][j-1]+a[i][j+1]
        line.append(value)
    a[i+1]=line
print(sum(a[N])%1000000000)
