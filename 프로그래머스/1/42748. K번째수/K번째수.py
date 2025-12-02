answer = []
def solution(array, commands):
    for command in commands:
        i,j, k = command #리스트 그냥 값 할당하기
        tmp = array[i-1:j]

        tmp.sort()
        answer.append(tmp[k-1])
    return answer