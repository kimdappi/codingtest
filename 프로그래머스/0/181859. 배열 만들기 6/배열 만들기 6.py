def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        # 1. stk이 비어있으면 현재 원소 추가
        if not stk:
            stk.append(arr[i])
        # 2. stk의 마지막 원소가 arr[i]와 같으면 마지막 원소 제거
        elif stk[-1] == arr[i]:
            stk.pop()
        # 3. stk의 마지막 원소가 arr[i]와 다르면 현재 원소 추가
        else:
            stk.append(arr[i])
            
    # 작업을 마친 후 stk이 비어있으면 [-1], 아니면 stk 반환
    return stk if stk else [-1]