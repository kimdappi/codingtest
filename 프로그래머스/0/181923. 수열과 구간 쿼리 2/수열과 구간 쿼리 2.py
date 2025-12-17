def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        candidates = [x for x in arr[s:e+1] if x > k]
        answer.append(min(candidates) if candidates else -1)
    return answer
