import math
t = int(input())

#원의 접점을 구하는 것은 두점사이의 거리가 반지름간의 
# 합보다 작고 차보다 커야 2개의 접점이 생김
for i in range(t):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split(' ')))
    distance = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    rs=r1+r2
    rm =abs(r1-r2)

    if distance ==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if distance==rs or distance==rm:
            print(1)
        elif distance<rs and distance>rm:
            print(2)
        else:
            print(0)