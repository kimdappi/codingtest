def solution(myString):
    answer=''
    for i in myString:
        if i.islower():
            i=i.upper()
        answer+=i
    return answer            