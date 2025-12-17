def solution(arr, queries):
    answer = arr.copy()
    for i, j in queries:
        answer[i], answer[j] = answer[j], answer[i]
    return answer
