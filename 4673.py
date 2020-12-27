
def d(n):
    v_list = list(str(n))
    new_value=0
    for i in v_list:
        new_value+=int(i)
    new_value+=n
    result[new_value]=1

result = [0]*100000
for i in range(1,10001):
    d(i)
        
for i in range(1,10001):
    if result[i]==0:
        print(i)
