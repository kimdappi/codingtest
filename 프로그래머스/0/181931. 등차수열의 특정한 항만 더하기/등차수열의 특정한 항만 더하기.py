
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        suma = a + d * i
        if included[i]:
            answer += suma
    return answer
            
            