n,m = list(map(int,input().split(' ')))
def num_count(x, y):
    count = 0
    while x!=0:
        x=x//y
        count+=x
    return count

print(min(num_count(n,2)-num_count(m,2)-num_count(n-m,2),
num_count(n,5)-num_count(m,5)-num_count(n-m,5)))

