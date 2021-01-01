import math
#remove는 return이 없다.
while True:
    x,y,z = list(map(int,input().split(' ')))
    if x==0 and y==0 and z==0:
        break
    line = [x,y,z]
    num1=min(line)
    line.remove(min(line))
    num2=min(line)
    line.remove(min(line))
    if math.pow(line[0],2)==math.pow(num1,2)+math.pow(num2,2):
        print('right')
    else:
        print('wrong')

    