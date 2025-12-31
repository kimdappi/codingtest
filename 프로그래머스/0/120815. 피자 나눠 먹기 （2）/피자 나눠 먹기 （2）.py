"""
n - 나눠먹을 사람 수
정확히 떨어지려면 몇 판 시켜야하는지?
한 판에 6개
"""
def solution(n):
    pizza = 1
    while True:
        if (pizza * 6)%n ==0:
            return pizza
        else:
            pizza+=1
        
