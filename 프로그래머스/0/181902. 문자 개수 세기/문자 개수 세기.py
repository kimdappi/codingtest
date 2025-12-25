def solution(my_string):
    # 52개의 0으로 초기화된 배열 생성
    answer = [0] * 52
    
    for char in my_string:
        if char.isupper():
            # 대문자인 경우: 'A'의 아스키 값을 빼서 0~25 인덱스에 저장
            answer[ord(char) - ord('A')] += 1
        else:
            # 소문자인 경우: 'a'의 아스키 값을 빼고 26을 더해 26~51 인덱스에 저장
            answer[ord(char) - ord('a') + 26] += 1
            
    return answer