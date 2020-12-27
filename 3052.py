a=set()
for i in range(10):
    num=int(input())
    div = num%42
    a.add(div)

print(len(a))