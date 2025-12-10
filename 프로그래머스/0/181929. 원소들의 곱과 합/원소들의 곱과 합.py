def solution(num_list):
    mul=1
    sqr= 0
    for i in num_list:
        mul*=i
        sqr+=i
    sqr=sqr**2
    if mul<sqr:
        return 1
    else:
        return 0