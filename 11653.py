n=int(input())
cnt=2
if n==1:
    exit()
while True:
    if n==1:
        break
    if n%cnt==0:
        print(cnt)
        n/=cnt
    else:
        cnt+=1

