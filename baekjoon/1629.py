"""
1. 아이디어
A를 B번 곱하고, 이를 C로 나눈 나머지를 구함
output A ^ B %C

2. 시간복잡도
 (O(log b))
재귀를 써서 그리디보다는 적어질 수 있음
여기서 C를 나중에 빼지 않고 재귀 함수 안에 넣는 게 중요함

3. 자료구조


"""

import sys
input = sys.stdin.readline

]def power(a, b, c):
    # 1. 기저 조건: b가 0이면 결과는 1
    if b == 0:
        return 1

    temp = power(a, b // 2, c)
    result = (temp * temp) % c

    # 4. 지수가 홀수일 때: a를 한 번 더 곱함
    if b % 2 == 1:
        result = (result * a) % c

    return result

a, b, c = map(int, input().split())
output = power(a, b, c)

print(output)
