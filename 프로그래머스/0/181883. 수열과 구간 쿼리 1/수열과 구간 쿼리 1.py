def solution(arr, queries):
    # 1. queries에 있는 각 query [s, e]를 하나씩 가져옵니다.
    for s, e in queries:
        # 2. s부터 e까지 (e를 포함해야 하므로 e+1) 반복합니다.
        for i in range(s, e + 1):
            # 3. 해당 인덱스의 값을 1 증가시킵니다.
            arr[i] += 1
            
    # 4. 모든 처리가 끝난 arr을 반환합니다.
    return arr