string ='as..efs...fesf..fse.'
cnt = 0
temp=''
for i in range(len(string)):
    
    if string[i]=='.':
        cnt+=1
    else:
        if cnt==0:
            temp+=string[i]
        else:
            temp+='.'
        cnt=0
