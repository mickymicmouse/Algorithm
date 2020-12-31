N = int(input())
fibo = [0]*(N+2)
fibo[1]=1
fibo[2]=1
cnt = 3
while True:
    if fibo[N]!=0:
        break
    fibo[cnt]=fibo[cnt-1]+fibo[cnt-2]
    cnt+=1
print(fibo[N])    