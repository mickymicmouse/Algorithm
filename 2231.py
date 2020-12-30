N = int(input())
result=False
for i in range(1, N+1):
    string = str(i)
    num = i
    for j in string:
        num+=int(j)
    if num == N:
        result=True
        print(i)
        break
if result==False:
    print(0)

