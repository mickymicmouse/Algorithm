t = int(input())
#중요도가 같은 경우를 생각하지 않았기 때문에 fail
for ss in range(t):
    n, m = map(int,input().split(' '))
    d = list(map(int,input().split(' ')))
    k=[]
    for i in range(len(d)):
        k.append((i,d[i]))

    k.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(k)):
        x,y = k[i]
        if x==m:
            print(i+1)

