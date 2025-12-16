def solution(strArr):
    i=0
    answer=[]
    for s in strArr:
        if i%2==0:
            a=s.lower()
            answer.append(a)
        else:
            a=s.upper()
            answer.append(a)
        i+=1
    return answer
            