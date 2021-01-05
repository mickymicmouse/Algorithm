import datetime

start = datetime.datetime.now()
string = list(map(str, input().strip()))
n=len(string)

def expand(left, right):
    while left>=0 and right<=len(string) and string[left] == string[right-1]:
        left -= 1
        right +=1
    return string[left+1:right-1]

if len(string)<2 or string[::-1]==string:
    print(string)
    exit()

result = ''
for i in range(len(string)-1):
    result = max(result, expand(i,i+1), expand(i,i+2), key = len)

print(result)
finish = datetime.datetime.now()
print(finish-start)

