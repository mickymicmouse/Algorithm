h,m = map(int,input().split(' '))


if m<45:
    if h==0:
        result_hour = 23
        result_minute = 60-(45-m)
    else:
        result_hour = h-1
        result_minute = 60-(45-m)

else:
    result_hour = h
    result_minute = m-45
print(result_hour, result_minute)