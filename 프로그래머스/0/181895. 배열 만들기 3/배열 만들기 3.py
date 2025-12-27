def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        answer.append(arr[a:b+1])
    
    return sum(answer,[])