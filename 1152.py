string = input().strip().upper().split(' ')
# 공백이 들어오는 경우를 확인해 주어야 함
if string==['']:
    print(0)
    exit()
else:
    print(len(string))
