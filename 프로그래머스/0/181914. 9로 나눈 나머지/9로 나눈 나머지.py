def solution(number):
    answer = 0
    ltofnum=map(int,list(number))
    answer=sum(ltofnum)%9
    return answer