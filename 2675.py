N = int(input())
for i in range(N):
    string = ''
    n,a = input().split(' ')
    n=int(n)
    a=list(map(str,a))
    for i in a:
        new = i*n
        string+=new
    print(new)