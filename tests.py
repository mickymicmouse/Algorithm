# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)


result = dict()
model =dict()
prune = dict()
n = int(input().strip())
train = []
train_eval = []
for i in range(n):
    ability = list(map(float, input().strip().split(' ')))
    train.append(ability[:12])
    train_eval.append(ability[12])
t = int(input().strip())
test=[]
for i in range(t):
    test.append(list(map(float, input().strip().split(' '))))

def var(data):
    if len(data)==0:
        return 0
    mean = sum(data)/len(data)
    s_var = 0
    for i in data:
        s_var = s_var+(i-mean)**2
    v = s_var/len(data)
    return v
   
def split(stand ,col, data, data_label):
    x_small=[]
    x_large=[]
    y_small=[]
    y_large=[]
    for row in range(len(data)):
        if data[row][col]>stand:
            x_large.append(data[row])
            y_large.append(data_label[row])
        else:
            x_small.append(data[row])
            y_small.append(data_label[row])
    
    r = (-1)*var(y_small)*sum(y_small)+(-1)*var(y_large)*sum(y_large)
    return x_small, x_large, y_small, y_large, r
    
    
def DT(max_depth,cur_depth, train, train_eval, count):
    
    global model, result, prune
    if len(train_eval)==0:
        return
    if max_depth==cur_depth: # 최대 깊이 트리일 경우
        result[count]=sum(train_eval)/len(train_eval) #결과가 저장된 딕셔너리
        return

    if var(train_eval)==0:
        result[count]=sum(train_eval)/len(train_eval)
        return
    x = (-1)*float('inf')
    for i in range(len(train)): #선수
        for j in range(len(train[0])): # 능력치
            x_s, x_l,y_s,y_l, rij = split(train[i][j], j, train, train_eval)
            if rij>=x:
                x=rij
                x_small=x_s
                x_large=x_l
                y_small=y_s
                y_large=y_l
                c = train[i][j]
                cj = j
                ci = i
                
    model[count]=c #기준점 정리된 딕셔너리
    prune[count]=cj
    DT(max_depth, cur_depth+1, x_small,y_small,count+'left')
    DT(max_depth, cur_depth+1, x_large,y_large, count+'right')

    return

def predict(max_depth, model, result,prune, test):
    y_pred=[]
    for row in range(len(test)):
        seq='head'

        for cur_depth in range(max_depth-1):
            if model[seq]<test[row][prune[seq]]:
                seq+='right'
            else:
                seq+='left'
        while True:
            if model.get(seq):
                break
            else:
                if seq[-2]=='h':
                    seq = seq[:-5]
                else:
                    seq = seq[:-4]
        y_pred.append(result[seq])
    
    return y_pred
    
count = 'head'

DT(6, 1, train, train_eval, count)
y_pred = predict(6, model, result, prune, test)
for i in y_pred:
    print("{:.3f}".format(i))



print("{:.3f}".format(3.141582))

model.get('x')


import random
random.seed(a=100)
l = [1,2,3,4,5,6,7,8,9]
random.sample(l,3)


a = [1,1,2,3]
unique(a)

a="java and backend and junior and pizza 100"
a.replace(' and ','&')
a.remove('java')