a=[]
max_value=0
max_index=0
for i in range(9):
    a.append(int(input()))
    if max(a)>max_value:
        max_index=i+1
        max_value = max(a)

print(max_value)
print(max_index)