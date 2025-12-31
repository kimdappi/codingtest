import math
def solution(n):
    answer = 0
    if n>=7:
        answer=math.ceil(n/7)
    elif n<=7:
        answer=1
    return answer