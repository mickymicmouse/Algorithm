k = int(input())
for i in range(k):
    H,W,N=map(int, input().split(' '))
    if N%H==0:
        floor = str(H)
        row = N//H
    else:
        floor = str(N%H)
        row = N//H+1
    if row<10:
        row='0'+str(row)
    else:
        row = str(row)
    
    room=floor+row
    print(room)
    