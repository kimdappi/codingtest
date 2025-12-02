def solution(participant, completion):
    hash_map = {}
    
    # 1) 참가자 이름 카운트
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1

    # 2) 완주자 이름 카운트 줄이기 (매칭되는 사람 제거)
    for c in completion:
        hash_map[c] -= 1
    
    # 3) 값이 1인 사람이 완주 못한 선수
    for name, count in hash_map.items():
        if count > 0:
            return name
