import sys
input=sys.stdin.readline
sys.setrecursionlimit(20000)

n = int(input())
square = [list(map(int,input().strip())) for _ in range(n)]
w_count=0
b_count=0
result=''

def quard(x,y,w):
    global w_count, b_count, result
    num = w**2
    b_num=0
    w_num=0
    for i in range(x,x+w):
        for j in range(y,y+w):
            if square[i][j]==1:
                b_num+=1
            else:
                w_num+=1
    
    if b_num==num:
        result+='1'
        return
    elif w_num==num:
        result+='0'
        return
    else:
        for i in range(2):
            for j in range(2):
                if i==0 and j==0:
                    result+='('
                quard(x+(w//2)*i, y+(w//2)*j, w//2)
                if i==1 and j==1:
                    result+=')'
    return 

quard(0,0,n)
print(result)
    

