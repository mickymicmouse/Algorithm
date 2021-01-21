n = int(input())
line = list(map(int,input().split(' ')))
x = int(input())
line.sort()
start = 0
end = n-1
count=0
while True:
    if start>=end:
        break
    if line[start]+line[end]==x:
        count+=1
        start+=1
        end-=1
    elif line[start]+line[end]>x:
        end-=1
    else:
        start+=1
print(count)

