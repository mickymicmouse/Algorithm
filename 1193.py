X = int(input())

k=1
while True:
    if X<=k:
        break
    X-=k
    k+=1
if k%2==0:
    a=X
    b=k-X+1
else:
    a=k-X+1
    b=X
print(a,'/',b, sep='')

#어렵다리...
