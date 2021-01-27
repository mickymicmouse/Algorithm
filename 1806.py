n,s = map(int,input().split(' '))
line = list(map(int,input().split(' ')))
left=right=total=cnt=0
result = n
flag = False
while True:
    if total>=s:
        flag = True
        result=min(result,cnt)
        total-=line[left]
        left+=1
        cnt-=1
    elif right==n:
        break
    else:
        total+=line[right]
        right+=1
        cnt+=1
if flag:
    print(result)
else:
    print(0)
