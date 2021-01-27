import math
n,m = map(int,input().split(' '))
sq = [list(map(int,input())) for _ in range(n)]
ans=-1
for i in range(n):
    for j in range(m):
        for i_d in range(-n,n):
            for j_d in range(-m,m):
                if i_d == 0 and j_d == 0:
                    continue
                string = []
                row = i
                col = j
                while (0<=row<n) and (0<=col<m):
                    string.append(sq[row][col])
                    s=''
                    for k in string:
                        s+=str(k)
                    val = math.sqrt(int(s))

                    if val == int(val):
                        ans = max(ans,int(val)**2)
                    row+=i_d
                    col+=j_d
print(ans)