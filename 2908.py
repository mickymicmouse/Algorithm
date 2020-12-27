a,b =list(map(str, input().split(' ')))
a=list(a)
b=list(b)
new_a=''
new_b=''
for i in range(len(a)-1,-1,-1):
    new_a+=a[i]
for i in range(len(b)-1,-1,-1):
    new_b+=b[i]
new_a = int(new_a)
new_b = int(new_b)
print(max(new_a, new_b))