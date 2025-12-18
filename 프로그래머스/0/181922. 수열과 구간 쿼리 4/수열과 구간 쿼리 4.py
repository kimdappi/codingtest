"""
i가 k의 배수 -> arr[i]에 +=1
"""
def solution(arr, queries):
    for s,e,k in queries:
        start = ((s+k-1)//k)*k
        for i in range(start, e+1,k):
            arr[i]+=1
    return arr