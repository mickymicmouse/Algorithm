x=[]
y=[]
# 네이버 부스트캠프 데모문제
for i in range(3):
    x_,y_ = list(map(int,input().split(' ')))
    x.append(x_)
    y.append(y_)
for i in x:
    if x.count(i)!=2:
        print(i,end=' ')
for i in y:
    if y.count(i)!=2:
        print(i)
