def solution(num_list):
    n = len(num_list)
    
    if n >= 11:
        return sum(num_list)
    
    else:
        answer = 1
        for x in num_list:
            answer *= x
        return answer