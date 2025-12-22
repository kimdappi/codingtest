def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
"""
my_string[s:e+1][::-1] -> 문자열 슬라이싱하고 뒤집기
"""