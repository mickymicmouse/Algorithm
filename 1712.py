A,B,C = map(int,input().split(' '))
count =0
if B>=C:
    print(-1)
    exit()
else:
    print((A//(C-B))+1)
""" while True:
    try:

        count+=1
        minus=A+count*B
        plus = count*C
        if plus>minus:
            print(count)
            break
    except:
        break """
        #주석 처리는 alt  + shift + A
        