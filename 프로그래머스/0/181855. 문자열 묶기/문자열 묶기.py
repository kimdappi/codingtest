"""
기존에 풀던 방식으로 풀이...
dict로 삽입
"""
def solution(strArr):
    answer = 0
    len_arr={}
    for arr in strArr:
        length=len(arr)
        if length in len_arr:
            len_arr[length]+=1
        else:
            len_arr[length]=1
    return max(len_arr.values())