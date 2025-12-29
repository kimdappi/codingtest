"""
값 >=50 이면 /2
else면 *2
"""
def solution(arr):
    answer=[]
    for ab in arr:
        if ab>=50 and ab%2==0:
            answer.append(ab//2)
        elif ab <50 and ab%2==1:
            answer.append(ab*2)
        else:
            answer.append(ab)
    return answer
            