import sys
input=sys.stdin.readline
t = int(input())
for i in range(t):
    string = list(map(str,input().strip()))
    count = [0]*len(string)
    flag=False
    if len(string)%2==0:
        if string[0]=='(' and string[-1]==')':
            if string.count('(')==string.count(')'):
                count[0]=1
                for j in range(1,len(string)):
                    if string[j]=='(':
                        count[j]=count[j-1]+1
                    else:
                        count[j]=count[j-1]-1
                for s in count:
                    if s<0:
                        print('NO')
                        flag=True
                        break
                if flag==False:
                    print('YES')
            
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')