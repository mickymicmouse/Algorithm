b = list(input())

def judge():
    q=[]
    for i in b:
        if (i==')' or i==']') and not q:
            return False
        if i==')':
            val = q.pop()
            if val!='(':
                return False
        elif i==']':
            val = q.pop()
            if val!='[':
                return False
        else:
            q.append(i)
    if not q:
        return True
    else:
        return False

def inner(equation):
    s=''
    for _ in equation[:-2]:
        s+=_
    sums=eval(s)
    t = eval(str(sums)+equation[-2]+equation[-1])
    print(s)
    return t




def solve(ss):
    stack=[]
    for s in ss:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')':
            if stack[-1] =='(':
                stack[-1]=2
            else:
                tmp=0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i] == '(':
                        stack[-1] = tmp*2
                        break
                    else:
                        tmp+=stack[i]
                        stack=stack[:-1]
        elif s==']':
            if stack[-1]=='[':
                stack[-1]=3
            else:
                tmp = 0
                for i in range(len(stack)-1,-1,-1):
                    if stack[i]=='[':
                        stack[-1]=tmp*3
                        break
                    else:
                        tmp+=stack[i]
                        stack=stack[:-1]
    return sum(stack)

        
    
    

re = judge()
if re:
    print(solve(b))
else:
    print(0)
    exit()



