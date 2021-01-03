n=int(input())
dist = list(map(int,input().split(' ')))
oil = list(map(int,input().split(' ')))
start=0
cnt=1
checking=0
money=dist[0]*oil[0]
while True:
    if n-2==checking:
        break
    if oil[start]<oil[cnt]:
        money+=(oil[start]*dist[cnt])
        cnt+=1
    else:
        start=cnt
        cnt+=1
        money+=(oil[start]*dist[start])
    checking+=1
print(money)