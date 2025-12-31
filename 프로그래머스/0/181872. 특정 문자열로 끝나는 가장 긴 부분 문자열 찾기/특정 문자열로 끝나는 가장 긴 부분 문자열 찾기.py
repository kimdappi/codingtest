def solution(myString, pat):
    last_idx =myString.rfind(pat)
    return myString[:last_idx+len(pat)]