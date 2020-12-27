
"""
1 --> 1 
2 --> 11, 00
3 --> 100, 001, 111
4 --> 1100, 1001, 0011, 0000, 1111

홀수 -> 1 이 홀수개 들어감
짝수 -> 1 이 짝수개 들어감
"""


k=input()
n=int(k)


array = [0 for i in range(n)]
if n ==1:
    array[0]=1
    print(array[0])
elif n==2:
    array[1]=2
    print(array[1])
else:
    array[0]=1
    array[1]=2
    for i in range(2,n):
        array[i]=int(array[i-1])+int(array[i-2])
        array[i]=array[i]%15746

    result = array[i]
    print (result)






        



