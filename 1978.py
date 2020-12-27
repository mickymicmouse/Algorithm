N = int(input())
a = list(map(int,input().split(' ')))
notsosu = []
for i in range(len(a)):
    num = a[i]
    if num==1:
        notsosu.append(1)
        continue
    elif num==2:
        continue
    else:
        for j in range(2, num//2+1):
            if num%j==0:
                notsosu.append(num)
                break
        
print(len(a)-len(notsosu))