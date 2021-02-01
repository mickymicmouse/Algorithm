import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy
n,m,d = map(int,input().split(' '))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

square=[list(map(int,input().split(' '))) for _ in range(n)]
positions = list(combinations([i for i in range(m)],3))

def cal_dis(a1,b1,a2,b2):
    return abs(a1-a2)+abs(b1-b2)

def shooting(row, col):
    e_list=[]
    for k in range(row-1, -1,-1): #거리 역순으로
        for h in range(m): # 열 개수
            if square_copy[k][h] == 1:
                distance = cal_dis(row,col,k,h)
                if distance<=d:
                    e_list.append((distance,k,h))
    if e_list:
        e_list.sort(key=lambda x:(x[0],x[2]))
        enemy.append((e_list[0][1], e_list[0][2]))
        return True
    return False

enemy=[]
total_result=0
shoot =0
for pos in positions:
    result=0
    square_copy = copy.deepcopy(square)
    for i in range(n, 0,-1): # 가까운 행부터 체크
        for j in pos:  # 궁수들 열
            if shoot<3:
                flag = shooting(i,j)
                if flag:
                    shoot+=1
        shoot=0
        for f in enemy:
            if square_copy[f[0]][f[1]] == 1:
                result+=1
                square_copy[f[0]][f[1]] = 0
        enemy.clear()
    if total_result < result:
        total_result = result
print(total_result)
 







