t = int(input())
for i in range(t):
    n=int(input())
    cloth = dict()
    a = []
    num=0
    for i in range(n):
        k,s = input().split(' ')
        a.append((k,s))
        cloth[s]=[]
    for i,j in a:
        cloth[j].append(i)
    result=1
    for i in cloth.keys():
        result*=(len(cloth[i])+1)
    print(result-1)

        
        


    
