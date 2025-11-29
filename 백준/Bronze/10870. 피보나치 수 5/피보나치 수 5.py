"""
재귀 연습

"""
a = int(input())

def fibo(num):
    if num<=1:
        return num
    return fibo(num-1)+fibo(num-2)
## 우선 냅다 부르는거므로, 사고흐름과 역순으로 갈 수 있다.
## 재귀함수가 헷갈리는 이유가, 스칼라값을 부르는게 아니라 함수를 부르기 때문이다.
print(fibo(a))