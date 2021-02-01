import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
square = [list(map(int,input().split(' '))) for _ in range(n)]
b_count=0
w_count=0
def cut(x,y,w):
    global b_count
    global w_count
    num = w**2
    num_b=0
    num_w=0
    for i in range(x,x+w):
        for j in range(y,y+w):
            if square[i][j]==0:
                num_w+=1
            else:
                num_b+=1
    if num_w==num:
        w_count+=1
        return
    elif num_b==num:
        b_count+=1
        return
    else:
        for i in range(2):
            for j in range(2):
                a = x+(w//2)*i
                b = y+(w//2)*j
                cut(a,b,w//2)

cut(0,0,n)
print(w_count)
print(b_count)