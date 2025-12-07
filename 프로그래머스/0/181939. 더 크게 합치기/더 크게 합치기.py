def solution(a, b):
    a=str(a)
    b=str(b)
    c=int(a+b)
    d=int(b+a)
    return max(c,d)