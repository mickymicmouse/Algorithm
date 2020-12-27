string = list(input().upper())
alpha=[]
for i in range(65,91):
    alpha.append(chr(i))
count=[0]*len(alpha)
for i in range(len(alpha)):
    count[i]=string.count(alpha[i])
if count.count(max(count))>=2:
    print('?')
else:
    j = count.index(max(count))
    print(alpha[j])