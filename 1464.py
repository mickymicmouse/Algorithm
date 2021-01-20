import sys

S=list(input().strip())

ans=S[0]

for i in range(1,len(S)):
    if S[i]<=ans[0]:
        ans=S[i]+ans

    else:
        ans+=S[i]

print(ans)


