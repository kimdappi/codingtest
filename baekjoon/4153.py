# 4153
import sys
input = sys.stdin.readline

while True:
    num_list = list(map(int, input().split()))

    if sum(num_list)==0:
        break

    num_list.sort()
    a,b,c = num_list

    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")
