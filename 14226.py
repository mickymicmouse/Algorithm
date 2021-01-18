s=int(input())
ch = [[-1]*(s+1) for _ in range(s+1)]


#x = 화면의 개수
#y = 클립보드의 개수
#풀이 팁: bfs로 푸는데 클립보드와 화면의 이모티콘 개수를 배열로 만들어서 3가지 연산의 결과를 
#각각 기준으로 제작한 뒤 bfs로 돌리면 만들어진 행렬안에 최소경로가 나타나게됨.

def bfs():
    result=float('inf')
    q=[]
    q.append((1,0))
    ch[1][0]=0
    while q:
        x,y = q.pop(0)
        if ch[x][x]==-1: #1번연산관련
            ch[x][x]=ch[x][y]+1
            q.append((x,x))
        if x+y<=s and ch[x+y][y]==-1: #2번 연산 관련
            ch[x+y][y]=ch[x][y]+1
            q.append((x+y,y))
        if x-1>=0 and ch[x-1][y]==-1: #3번 연산 관련
            ch[x-1][y]=ch[x][y]+1
            q.append((x-1,y))
        if x==s:
            result = min(result, ch[x][y])
    return result
        

print(bfs())


