def solution(myString):
    answer = ''
    for item in myString:
        if item=='a':
            answer+='A'
        elif item =='A':
            answer+=item
        else:
            answer+=item.lower()
    return answer