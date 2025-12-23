def solution(myString):
    answer= myString.split('x')
    answer.sort()
    sample_list = ' '.join(answer).split()
    return sample_list