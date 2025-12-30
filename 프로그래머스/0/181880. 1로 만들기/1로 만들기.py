def solution(num_list):
    answer = 0
    for item in num_list:
        while item > 1:
            if item%2==0:
                item=item//2
            else:
                item= (item-1)//2
            answer+=1
            
    return answer