n = int(input())
words = [input() for _ in range(n)]
words.sort()
words.sort(key=len)
for i in range(n-1,0,-1):
    if words[i]==words[i-1]:
        words.pop(i)
for i in words:
    
    print(i)