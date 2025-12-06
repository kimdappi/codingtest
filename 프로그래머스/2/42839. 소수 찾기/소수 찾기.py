from itertools import permutations


def solution(numbers):
    prime_set = set()
    
    # 1. 모든 숫자 조합을 만든다.
    for i in range(len(numbers)):
        #print(list(numbers)) ## 문자열을 리스트로 casting하면 한 글자씩.
        numbers_permutation = permutations(list(numbers), i+1)
        #print(list(numbers_permutation))
        #print(list(map("".join,numbers_permutation)))
        numbers_perm_list =map(int, map("".join,numbers_permutation))
        prime_set |= set(numbers_perm_list) #union 연산자, 업데이트의 의미로 사용
        
    # 2. 소수가 아닌 수 제외
    prime_set -=set(range(0,2)) # 0,1 제외하고 시작
    lim = int(max(prime_set) **0.5)+1 #에라토스테네스의 체
    for i in range(2,lim):
        prime_set -= set(range(i*2,max(prime_set)+1,i))
    return len(prime_set)
print(solution("17"))