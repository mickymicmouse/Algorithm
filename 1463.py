N = int(input())
cnt=0
a=dict()
a[0]=[]
a[0].append(N)
check=[N]
while True:
    if 1 in check:
        break
    cnt+=1
    a[cnt]=[]
    for i in range(len(a[cnt-1])):
        value = a[cnt-1][i]
        if value%3==0:
            a[cnt].append(value//3)
        if value%2==0:
            a[cnt].append(value//2)
        a[cnt].append(value-1)
    check.extend(a[cnt])
print(cnt)

