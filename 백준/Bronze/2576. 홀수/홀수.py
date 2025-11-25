"""
1. 아이디어
- 7개 for문으로 input 받고
- 출력은 2개
- 홀수 합
- 홀수 중 최솟값

2. 시간복잡도
O(n) -> 어차피 7개라 상관 없음

3. 자료구조
리스트로 인풋 구하기
"""
import sys
input = sys.stdin.readline
A = [int(input()) for _ in range(7)] ## 너무 어색한데.

summation = 0
odd_list = []

for x in A:
    if x %2==1:
        summation +=x
        odd_list.append(x)

if summation == 0:
    print(-1)
else:
    print(summation)
    print(min(odd_list))
