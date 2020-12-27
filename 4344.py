N = int(input())
for i in range(N):
    line = list(map(int,input().split(' ')))
    line.pop(0)
    mean = sum(line)/len(line)
    count=0
    for i in line:
        if i > mean:
            count+=1
    per = count*100/len(line)
    print('%.3f%%'%per)