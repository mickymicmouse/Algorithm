N = int(input())
count=0
for i in range(N):
    alpha=[]
    check=[]
    for j in range(97,123):
        alpha.append(chr(j))
        check.append(1)
    string = list(map(str,input()))
    
    for j in range(len(string)):
        if j==0:
            check[alpha.index(string[j])]-=1
        else:
            if string[j-1]==string[j]:
                continue
            else:
                check[alpha.index(string[j])]-=1
    if check.count(1)+check.count(0)==len(alpha):
        count+=1
print(count)

# if list(string) == sorted(string, string.find()) 사용할 경우 word에서 나오는 대로 정렬되서 코딩이 쉬워짐