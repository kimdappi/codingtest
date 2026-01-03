def solution(myStr):
    s = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    answer = s.split() 
    return answer if answer else ["EMPTY"]