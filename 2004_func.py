n,m=list(map(int,input().split(' ')))
num1 = 1
num2 = 1
for i in range(n-m,n+1):
    num1*=i
for i in range(1, m+1):
    num2*=i
count=0
while num1!=0:
    num1-=num2
    count+=1

num4 = str(count)
result=0
for i in range(len(num4)-1,-1,-1):
    if num4[i]=='0':
        result+=1
    else:
        break
print(result)

#함수형식은 시간초과