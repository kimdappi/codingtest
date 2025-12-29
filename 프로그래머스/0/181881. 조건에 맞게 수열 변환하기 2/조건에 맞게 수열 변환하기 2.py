def solution(arr):
    answer = 0
    while True: ## 무한루프 돌리겠다는 뜻

        next_arr = []
        for item in arr:
            if item >= 50 and item % 2 == 0:
                next_arr.append(item // 2)
            elif item < 50 and item % 2 == 1:
                next_arr.append(item * 2 + 1)
            else:
                next_arr.append(item)
        
        if arr == next_arr:
            return answer
        
        arr = next_arr
        answer += 1