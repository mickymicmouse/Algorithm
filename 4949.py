
while True:
    line = input()
    if line=='.':
        break
    stack=[]
    flag = True
    for i in line:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)==0 or stack[-1]!='(':
                flag=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i==']':
            if len(stack)==0 or stack[-1]!='[':
                flag = False
                break
            elif stack[-1]=='[':
                stack.pop()
    if flag and len(stack)==0:
        print('yes')
    else:
        print('no')
