from collections import Counter

def solution(array):
    count_dict = Counter(array)
    
    # 상위 2개의 (값, 개수) 세트를 가져옵니다.
    common_items = count_dict.most_common(2)
    
    # 1. 데이터 종류가 하나뿐인 경우 (예: [1, 1, 1])
    if len(common_items) == 1:
        most_value, most_freq = common_items[0] # 첫 번째 세트만 꺼냄
        return most_value
    
    # 2. 데이터 종류가 여러 개인 경우 (각 세트를 변수에 할당)
    # 첫 번째로 많이 나온 정보
    first_value, first_freq = common_items[0]
    # 두 번째로 많이 나온 정보
    second_value, second_freq = common_items[1]
    
    # 가장 많이 나온 개수와 그다음으로 많이 나온 개수가 같다면?
    if first_freq == second_freq:
        return -1
    
    # 빈도가 다르다면 가장 많이 나온 값을 반환
    return first_value