def solution(myString):
    answer=[]
    demo= myString.split('x')
    for i in demo:
        answer.append(len(i))
    return answer
        