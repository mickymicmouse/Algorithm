N,M=map(int,input().split(' '))


def check(new_square):
    # B일때와 W일때를 case by case로 분할해서 풀어주어야함~ ㅋㅋ,,,
    basic_color = 'B'
    b_change=0
    for w in range(8):
        for h in range(8):
            if w%2==0 and h%2==0:
                # 왼쪽 위의 색깔과 동일
                if new_square[w][h]!=basic_color:
                    b_change+=1

            elif w%2!=0 and h%2!=0:
                # 왼쪽 위의 색깔과 동일
                if new_square[w][h]!=basic_color:
                    b_change+=1

            else:
                # 왼쪽 위의 색깔과 다름
                if new_square[w][h]==basic_color:
                    b_change+=1
    basic_color='W'
    w_change=0
    for w in range(8):
        for h in range(8):
            if w%2==0 and h%2==0:
                # 왼쪽 위의 색깔과 동일
                if new_square[w][h]!=basic_color:
                    w_change+=1

            elif w%2!=0 and h%2!=0:
                # 왼쪽 위의 색깔과 동일
                if new_square[w][h]!=basic_color:
                    w_change+=1

            else:
                # 왼쪽 위의 색깔과 다름
                if new_square[w][h]==basic_color:
                    w_change+=1
    return min(b_change, w_change)


        


square = []
for i in range(N):
    line = list(map(str, input()))
    square.append(line)

nums=[]
for i in range(N-7):
    for j in range(M-7):
        new_square = [z[j:j+8] for z in square[i:i+8]]
        nums.append(check(new_square))
print(min(nums))


        