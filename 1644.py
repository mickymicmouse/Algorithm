num = int(input())

def prime_list(n):
    sieve = [True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]==True:
            for j in range(i+i, n, i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]
A=prime_list(num)
left=right=total=cnt=0
while True:
    if total==num:
        print(left,right)
        cnt+=1
        total=0
        left=right=cnt
        
    elif total>num:
        total-=A[left]
        left+=1
    elif total<num:
        total+=A[right]
        right+=1
    if right==len(A):
        break
print(cnt)


    

        
