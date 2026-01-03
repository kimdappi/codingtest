def solution(arr):
    n = len(arr)
    target_length = 1
    
    while target_length < n:
        target_length *= 2

    answer = arr + [0] * (target_length - n)
    
    return answer