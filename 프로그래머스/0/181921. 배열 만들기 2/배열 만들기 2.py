from itertools import product

def solution(l, r):
    answer = []
    
    # 자릿수 범위
    min_len = len(str(l))
    max_len = len(str(r))
    
    for length in range(min_len, max_len + 1):
        # 0과 5로 이루어진 모든 조합
        for p in product(['0', '5'], repeat=length):
            # 맨 앞이 0이면 숫자 아님
            if p[0] == '0':
                continue
                
            num = int(''.join(p))
            
            if l <= num <= r:
                answer.append(num)
    
    if not answer:
        return [-1]
    
    return sorted(answer)
