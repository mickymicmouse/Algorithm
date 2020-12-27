T = int(input())
for i in range(T):
    x,y = map(int, input().split(' '))
    distance = y-x
    count = 0
    move = 1
    total_move = 0
    while True:
        if total_move>=distance:
            print(count)
            break
        count+=1
        total_move+=move
        if count%2==0:
            move+=1
        