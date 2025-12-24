"""
공백으로 split() 후 앞 뒤 값들은 int.
"""
def solution(binomial):
    num_list = binomial.split()
    a = int(num_list[0])
    b = int(num_list[2])
    op = num_list[1]
    if op =='+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b