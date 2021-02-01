while True:
    num = input()
    if num=='0':
        break
    start=0
    end=len(str(num))-1
    flag=True
    while True:
        if start>=end:
            break
        if num[start]!=num[end]:
            flag=False
            break
        start+=1
        end-=1
    if flag:
        print('yes')
    else:
        print('no')


