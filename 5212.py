r,c = map(int,input().split(' '))
sq =[]
sq.append(['.']*(c+2))
for i in range(r):
    line = ['.']+list(input().strip())+['.']
    sq.append(line)
sq.append(['.']*(c+2))
dp=[[0]*(c+2) for _ in range(r+2)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def check(x,y):
    count=0
    for s in range(4):
        nx = x+dx[s]
        ny = y+dy[s]
        if sq[nx][ny]=='.':
            count+=1
            if count>=3:
                return False
    return True

start_x=r+1
start_y=c+1
end_x = 0
end_y = 0  
for i in range(1,r+1):
    for j in range(1,c+1):
        if sq[i][j]=='X':
            flag = check(i,j)
            if flag:
                dp[i][j]=1
                start_x = min(start_x,i)
                start_y = min(start_y,j)
                end_x = max(end_x,i)
                end_y = max(end_y,j)
for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
        if dp[i][j]==0:
            sq[i][j]='.'
        print(sq[i][j], end='')
    print()



