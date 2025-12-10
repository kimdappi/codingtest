def solution(a, b, c):
    if a ==b and a ==c:
        return (a+b+c)*(a*a+b*b+c*c)*(a**3+b**3+c**3)
    elif a!=b and a!=c and b!=c:
        return a+b+c
    else:
        return (a+b+c)*(a*a+b*b+c*c)
        
    