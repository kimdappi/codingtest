# def solution(array, n):
#     answer = 0
#     a=0
#     for i in array:
#         if i==n:
#             answer+=1
    
#     return answer ## 코드가 너무 길고, 순회함.
def solution(array, n):
    count = {}
    for x in array:
        count[x] = count.get(x, 0) + 1
    return count.get(n, 0)
