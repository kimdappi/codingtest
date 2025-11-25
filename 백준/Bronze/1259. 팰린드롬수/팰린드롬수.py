import sys
input = sys.stdin.readline
str_list = []
while True:
    line = input().strip()
    if line == "0":
        break
    str_list.append(line)

result =[]

for X in str_list:
    if X== X[::-1]:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
