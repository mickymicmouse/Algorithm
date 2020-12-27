N= int(input())
for i in range(N):
    line = list(map(str,input()))
    score=[0]*len(line)
    count=0
    for s in range(len(line)):
        
        if line[s]=='O':
            count+=1
            score[s]=count
        else:
            count=0
    
    print(sum(score))
            




