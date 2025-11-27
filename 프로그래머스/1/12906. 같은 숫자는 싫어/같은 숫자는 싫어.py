def solution(arr):
    answer = []
    
    for x in arr:
        # answer가 비어 있거나, 마지막 값과 다를 때만 추가
        if not answer or answer[-1] != x:
            answer.append(x)
    
    return answer
