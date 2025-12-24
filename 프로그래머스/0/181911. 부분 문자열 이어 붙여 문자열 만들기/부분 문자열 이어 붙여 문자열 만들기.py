def solution(my_strings, parts):
    answer = []
    for s, (start, end) in zip(my_strings, parts):
        answer.append(s[start:end+1])  # end 포함이라 +1
    return ''.join(answer)
