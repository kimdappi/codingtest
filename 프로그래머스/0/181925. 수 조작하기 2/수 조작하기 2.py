"""
w +=1
s -=1
d +=10
a +=10
numlog = 결과값.

if i+1 - i == 1:
    result+='w'
"""

def solution(numLog):
    result = ''
    for i in range(len(numLog)-1):
        putalp=numLog[i+1]-numLog[i]
        if putalp==1:
            result+='w'
        elif putalp== -1:
            result+='s'
        elif putalp == 10:
            result +='d'
        else:
            result+='a'
    return result