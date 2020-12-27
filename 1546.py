a= int(input())
b= list(map(int,input().split()))
max_value = max(b)
c=[]
for i in range(len(b)):
    value = (b[i]/max_value)*100
    c.append(value)
mean = sum(c)/len(c)
print(mean)