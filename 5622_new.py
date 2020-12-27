dic = {2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6: 'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ'}
time = dict()
count=1
for i in range(9):
    count+=1
    time[i+1]=count

box = []
string = list(map(str,input()))
for i in range(len(string)):
    for num, word in dic.items():
        if string[i] in word:
            box.append(time[num])
            break
print(sum(box))
        