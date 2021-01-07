n,k = list(map(int,input().split(' ')))
num1 = 1
num2 = 1
for i in range(n,n-k,-1):
    num1*=i
for i in range(1,k+1):
    num2*=i
print(int(num1/num2))