def solution(num_list):
    index=0
    for i in num_list:
        if i<0:
            return index
        else:
            index+=1
    return -1