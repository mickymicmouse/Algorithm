A,B,V = map(int,input().split(' '))
count=0
while True:
    V-=A
    count+=1
    if V<=0:
        print(count)
        break
    V+=B

#시간 넘을듯
