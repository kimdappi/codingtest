"""
1. 입력  - 물건가격
2. 전체에서 물건 가격을 빼고,
그 가격으로 최대한 잔돈 금액 개수를 적게 가져가기
"""

import sys
input =sys.stdin.readline
cnt = 0
price = int(input())
balance = 1000 -price

coins = [500,100,50,10,5,1]
for each_coin in coins:
    cnt += balance //each_coin
    balance %= each_coin


print(cnt)
