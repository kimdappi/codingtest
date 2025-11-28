# from collections import deque

# def solution(prices):
#     answer = []
#     price_q=deque(prices)
#     #i가 2이면
#     for i in range(len(price_q)):
#         notfall=0
#         # 2 3 4
#         for j in range(i+1,len(price_q)):
#             notfall+=1
#             if price_q[i]>price_q[j]:
#                 break
#         answer.append(notfall)
#     return answer


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 아직 가격이 떨어지지 않은 시점의 인덱스

    for i in range(n):
        # 현재 가격이 스택에 있는 인덱스들의 가격보다 작으면
        # 그 시점에서는 가격이 떨어진 것
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j   # j에서 i까지 버틴 시간
        stack.append(i)

    # 끝까지 가격이 한 번도 안 떨어진 놈들 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer
