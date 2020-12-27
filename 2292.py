N = int(input())
array=[]
count=[]
n=1
k=1
array.append(1)
array.append(2)
if N==1:
    print(array[0])
    exit()
if 2<=N<8:
    print(array[1])
    exit()
if N>=8:
    while True:
        cal = 2+6*n
        array.append(cal)
        k+=1
        n+=k
        if cal>N:

            print(k)
            break

