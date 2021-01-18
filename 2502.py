d,k = list(map(int,input().split(' ')))
dp_x = [0]*31
dp_y = [0]*31
dp_x[3]=1
dp_y[3]=1
dp_x[4]=1
dp_y[4]=2
for i in range(5,31):
    dp_x[i]=dp_x[i-1]+dp_x[i-2]
    dp_y[i]=dp_y[i-1]+dp_y[i-2]

for j in range(k):
    value=(k-(dp_x[d]*j))%dp_y[d]
    result = (k-(dp_x[d]*j))//dp_y[d]
    if value==0:
        print(j)
        print(result)
        break