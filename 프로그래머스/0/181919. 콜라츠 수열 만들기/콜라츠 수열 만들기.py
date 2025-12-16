def solution(n):
    answer = [n]  # 1. 시작 숫자 n을 먼저 리스트에 담습니다.
    
    while n > 1:  # 2. n이 1이 되기 전까지 계속 반복합니다.
        if n % 2 == 0:
            n = n // 2      # 짝수일 경우: 2로 나눔
        else:
            n = 3 * n + 1   # 홀수일 경우: 3을 곱하고 1을 더함
            
        answer.append(n)    # 3. 계산된 값을 리스트에 추가합니다.
        
    return answer