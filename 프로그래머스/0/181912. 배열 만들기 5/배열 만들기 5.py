"""
배열 intstrs 각 원소별로 인덱스 s부터 l짜리 부분 문자열 잘라내서 정수로 변환
변환한 정수 값이 k보다 크면 담으면 됨.


"""
def solution(intStrs, k, s, l):
    answer=[]
    for arr in intStrs:
        a = int(arr[s:s+l])
        if a>k:
            answer.append(a)
    return answer