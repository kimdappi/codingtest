"""
제로 인덱스 아님
홀수번째 원소 합 짝수 번째 원소 합 둘 중 큰 거 return max로 출력
"""
def solution(num_list):
    even=0
    odd = 0
    for i in range(0,len(num_list),2):
        even+=num_list[i]
    for i in range(1,len(num_list),2):
        odd+=num_list[i]
    return max(even,odd)
        
        