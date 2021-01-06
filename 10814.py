n=int(input())
members=[]
for i in range(n):
    x,y = list(map(str, input().split(' ')))
    x=int(x)
    members.append((x,y))

members.sort(key=lambda x:x[0])
for i,j in members:
    print(i,j)