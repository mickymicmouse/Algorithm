s = list(input().strip().split(':'))
if len(s)==8:
    for i in range(len(s)):
        a = s[i]
        while True:
            if len(a)==4:
                break
            a='0'+a
        s[i] = a
else:
    c = 8-len(s)
    p = s.index('')
    for i in range(c):
        s.insert(p,'')
    for i in range(len(s)):
        a = s[i]
        while True:
            if len(a)==4:
                break
            a='0'+a
        s[i] = a
for i in range(8):
    if i!=7:
        print(s[i],end=':')
    else:
        print(s[i])

