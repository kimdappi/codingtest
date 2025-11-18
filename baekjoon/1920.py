"""
1920번
1. 아이디어
- n개 숫자 정렬
- m 개 for 돌면서 이진 탐색
- 이진탐색 안에서 마지막에 데이터 찾으면 1출력, 아니면 0출력

2. 시간복잡도
- n개 입력값 정렬 = o(nlgn)

3. 자료구조
- n개 숫자 배열
- m개 숫자 배열
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() #이진탐색 가능하게

def search(st,en,target):
    if st==en:
        if nums[st]==target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en)//2
    if nums[mid]<target:
        search(mid+1,en,target)
    else:
        search(st, mid, target)
for each_target in target_list:
    search(0,N-1,each_target)
