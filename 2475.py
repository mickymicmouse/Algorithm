a = list(map(int,input().split(' ')))
num=0
for i in a:
    num+=i**2
    result = num%10
print(result)