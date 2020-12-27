
while True:
    
    M = int(input())
    if M ==0:
        break
    num=0
    for i in range(M+1,2*M+1):
        if i == 1:
            continue
        elif i ==2:
            num+=1
            continue
        else:
            count=0
            for j in range(2, int((2*M+1)**0.5)+1):
                if i%j==0:
                    count+=1
                    break
            if count==0:
                num+=1
    print(num)
#시간초과가 남 그래서 에라토스테네스의 체를 사용해서 미리 소수를 모두 구해주어야함 
#참고는 4948_time.py
        