
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 북, 동, 남, 서 순으로

def move(op):
    global start_x
    global start_y
    global end_x
    global end_y
    global x
    global y
    if op=='F':
        x = x+dx[direction]
        y = y+dy[direction]
    elif op=='B':
        x = x-dx[direction]
        y = y-dy[direction]
    start_x = min(start_x,x)
    start_y = min(start_y,y)
    end_x = max(end_x, x)
    end_y = max(end_y, y)

def l_turn():
    global direction
    if direction==0:
        direction=3
    else:
        direction-=1
def r_turn():
    global direction
    if direction==3:
        direction=0
    else:
        direction+=1



for i in range(int(input())):
    s = list(input().strip())
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    direction=0
    x=y=0
    for j in s:
        if j=='F' or j=='B':
            move(j)
        elif j=='L':
            l_turn()
        elif j=='R':
            r_turn()
    if start_x==end_x or start_y==end_y:
        print(0)
    else:
        print(abs(end_x-start_x)*abs(end_y-start_y))
    