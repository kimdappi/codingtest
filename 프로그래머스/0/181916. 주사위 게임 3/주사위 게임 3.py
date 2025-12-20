"""
a b c d  다 같아?  1111*p
3같 1 다 -> (10*p + q)**2
2같 2같 -> (p+q)*abs(p-q)
2같 1다 1 다 -> q*r
다 다름 -> 제일 적은 숫자
"""

from collections import Counter

def solution(a, b, c, d):
    nums = [a, b, c, d]
    count = Counter(nums)
    values = sorted(count.values())

    if values == [4]:  # 4개 다 같음
        p = a
        return 1111 * p

    elif values == [1, 3]:  # 3같 1다
        for num, freq in count.items():
            if freq == 3:
                p = num
            else:
                q = num
        return (10 * p + q) ** 2

    elif values == [2, 2]:  # 2같 2같
        p, q = count.keys()
        return (p + q) * abs(p - q)

    elif values == [1, 1, 2]:  # 2같 1다 1다
        ones = [num for num, freq in count.items() if freq == 1]
        q, r = ones
        return q * r

    else:  # 다 다름
        return min(nums)
