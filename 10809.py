string = list(map(str,input()))
alpha = []

for i in range(97,123):
    alpha.append(chr(i))
for i in range(len(alpha)):
    if alpha[i] in string:

        index = string.index(alpha[i])
        print(index, end=' ')
    else:
        print(-1, end=' ')        
