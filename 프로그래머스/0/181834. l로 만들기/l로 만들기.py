def solution(myString):
    myString=list(myString)
    answer=''
    for i in myString:
        if ord(i) < ord('l'):
            a='l'
            answer+=a
        else:
            answer+=i
    return answer