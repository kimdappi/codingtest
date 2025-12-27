"""
query 순회하기
짝수 인덱스  -> 그 인덱스 제외하고 뒷부분 제거
홀수 -> 그 인덱스 제외하고 앞부분 제거

"""
def solution(arr, query):
    answer = arr.copy()
    idx=0
    for i in query:
        if idx%2==0:
            answer=answer[:i+1]
        else:
            answer=answer[i:]
        idx+=1
    return answer