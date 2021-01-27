# 산성 - 1 ~ 1,000,000,000
# 알칼리 - -1 ~ -1,000,000,000
# 두개 합쳐서 0에 가까운 용액 만들기

n = int(input())
line = list(map(int,input().split(' ')))
line.sort()
s = 0
e = n-1
result = float('inf')
result_x=0
result_y=0
while True:
    if s>=e:
        break
    b_val=line[s]+line[e]
    val = abs(b_val)
    if val<result:
        result_x=line[s]
        result_y=line[e]
        result = val
        if b_val>0:
            e-=1
        elif b_val<0:
            s+=1
        else:
            break
        
    else:
        if b_val>0:
            e-=1
        elif b_val<0:
            s+=1
        else:
            break
print(result_x, result_y)


    

        