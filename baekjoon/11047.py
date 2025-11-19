"""
1. 아이디어 : 동전 저장 뒤 반대로 뒤집음
- 동전 for >
    - 동전 사용개수 추가
    - 동전 사용한 만큼 K값 갱신

2. 시간 복잡도
- O(n)

3. 자료구조
- 동전금액 배열
- 동전 사용 개수
- 남은 금액

"""

import sys
input =sys.stdin.readline

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

cnt= 0

for each_coin in coins:
    cnt += K // each_coin
    K %= each_coin

print(cnt)



