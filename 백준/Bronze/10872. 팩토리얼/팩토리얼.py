"""
재귀 연습

"""
a = int(input())

def facto(num):
    result =1
    if num>0:
        result = num*facto(num-1)
    return result

print(facto(a))