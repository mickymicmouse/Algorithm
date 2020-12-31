T = int(input())
for i in range(T):
    N = int(input())
    P = [0]*(N+5)
    P[0]=1
    P[1]=1
    P[2]=1
    P[3]=1
    P[4]=2
    P[5]=2
    for i in range(6, N+1):
        P[i]=P[i-5]+P[i-1]
    print(P[N])

    