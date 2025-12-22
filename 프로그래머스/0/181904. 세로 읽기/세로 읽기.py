"""
2차원 배열로 어렵게 풀려고 했는데, 걍 점프를 잘하면 되는거였어
"""
def solution(my_string, m, c):

    answer = ""
    for i in range(c-1, len(my_string), m):  # c열은 인덱스로 c-1, 매 행마다 m씩 점프
        answer += my_string[i]
    return answer
