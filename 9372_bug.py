import sys
T=int(sys.stdin.readline())
 
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    for _ in range(M):
        a,b=map(int,sys.stdin.readline().split())
    print(N-1)

#모든 국가가 연결되어 있기 때문에 최소 연결 수인 N-1이 됨...이게뭐냐 ㅋㅋㅋ