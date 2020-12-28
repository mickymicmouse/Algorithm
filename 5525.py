N = int(input())
M = int(input())
S = input()

pattern = 0
result=0
count=1
for i in range(1, M-2,1):
    if S[count-1:count+2]=='IOI':
        pattern+=1
        if pattern == N:
            pattern-=1
            result+=1
        count+=1
    else:
        pattern=0
    count+=1
print(result)
        
