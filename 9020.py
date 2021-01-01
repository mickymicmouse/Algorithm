# 에라토스테네스의 체 = 루트n 까지 각 수의 배수가 되는 수들은 소수가 아니다.
import datetime
start = datetime.datetime.now()
sosu=[2,3]
for i in range(4, 10001):
    so = True
    for j in range(2, int((i**0.5)+1)):
        if i%j==0:
            so=False
            break
    if so==True:
        sosu.append(i)

finish = datetime.datetime.now()
finish-start

#에라토스테네스의 체
start = datetime.datetime.now()
sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1
finish = datetime.datetime.now()
finish-start

def check(a,b):
    if a in sosu and b in sosu:
        return int(a),int(b)
    else:
        return check(a-1,b+1)
    
T = int(input())
for i in range(T):
    n = int(input())
    num1, num2 = check(n/2,n/2)
    print(num1,num2)