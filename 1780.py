import sys
input = sys.stdin.readline
sys.setrecursionlimit(40000)

n = int(input())
square= [list(map(int,input().split(' '))) for _ in range(n)]

m_count=0
z_count=0
p_count=0

def cut(x,y,w):
    global m_count, z_count, p_count
    m_num=0
    z_num=0
    p_num=0
    num = w**2
    for i in range(x,x+w):
        for j in range(y,y+w):
            if square[i][j]==1:
                p_num+=1
            elif square[i][j]==0:
                z_num+=1
            else:
                m_num+=1
    
    if num==p_num:
        p_count+=1
        return
    elif num==z_num:
        z_count+=1
        return
    elif num==m_num:
        m_count+=1
        return 
    else:
        for i in range(3):
            for j in range(3):
                nw = w//3
                nx = x+(nw)*i
                ny = y+(nw)*j
                cut(nx,ny,nw)
    return

cut(0,0,n)
print(m_count)
print(z_count)
print(p_count)