"""
한 판당 조각 -> slice
사람수  n
조건 : 최소 한 조각 이상 꼬옥 남겨주기.
"""
def solution(slice, n):
    pizza =1
    while True:
        if (pizza*slice)//n >=1:
            return pizza
        else:
            pizza+=1