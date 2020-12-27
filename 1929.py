M,N = list(map(int,input().split(' ')))
for i in range(M,N+1):
    if i == 1:
        continue
    elif i==2:
        print(i)
        continue
    else:
        count=0
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                count+=1
                break
        if count==0:
            print(i)
        

