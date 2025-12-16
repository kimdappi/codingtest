def solution(my_string, alp):
    answer=''
    my_string=list(my_string)
    for i in my_string:
        if i==alp:
            a=i.upper()
            answer+=a
        else:
            answer+=i
    return answer