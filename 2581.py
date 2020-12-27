M = int(input())
N = int(input())
num=[] #전체 리스트이자 겨로가적으로 소수만 남음
for i in range(M,N+1):
    num.append(i)
    if i == 1:
        num.remove(i)
        continue
    elif i==2:
        
        continue
    else:
        for j in range(2, i//2+1):
            if i%j==0:
                num.remove(i)
                break
if len(num)==0:
    print(-1)
else:
    print(sum(num))
    print(min(num))
