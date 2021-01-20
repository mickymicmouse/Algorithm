import sys
input = sys.stdin.readline
from collections import deque
sq = []
for i in range(12):
    sq.append(list(input().strip()))
color = ['R','G','B','P','Y']

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#풀이방법 - chain을 .으로 바꾼 뒤 아래부터 비교해주는 과정을 통해 내려줄수 있도록 한다.

def bfs(x,y):
    q=deque()
    block.append((x,y))
    q.append((x,y))
    dp[x][y]=1
    val = sq[x][y]
    count=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<12 and 0<=ny<6:
                if dp[nx][ny]==0 and sq[nx][ny]==val:
                    q.append((nx,ny))
                    dp[nx][ny]=1
                    count+=1
                    block.append((nx,ny))


def fall():
    for w in range(6):
        for h in range(10,-1,-1):
            for k in range(11, h, -1):
                if sq[k][w]=='.' and sq[h][w]!='.':
                    sq[k][w]=sq[h][w]
                    sq[h][w]='.'
                    break
                
total_result=0
while True:
    result =False
    dp = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if sq[i][j] !='.' and dp[i][j]==0:
                block=[]
                bfs(i,j)
                if len(block)>3:
                    result=True
                    for cx,cy in block:
                        sq[cx][cy]='.'
                    

    if not result:
        break
    total_result+=1
    fall()
    
print(total_result)

                

    
