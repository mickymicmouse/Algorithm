a= int(input())
for i in range(a):
    b,c = map(int,input().split(' '))
    d = b+c
    print("Case #%d: %d"%(i+1,d))