# nCk = n! / (n-k)!k!
# 나머지 연산의 분배 법칙은 나눗셈에 대해 성립하지 않음
# 즉, 곱셈 형태로 바꾸어 주어야 함 (페르마 소 정리 사용)
# 페르마 소정리:
# a ^ p = a (mop p) (p: 소수, a: 정수)
# => a ^ (p - 2) = 1 / a (mop p)
# ... n! * ((n-k)!k!) ^ (p - 2)

def factorial(x):
    y = 1
    for i in range(2, x + 1):
        y = (y * i) % DIV
    return y
    # if x <= 1:
    #     return 1
    # return x * factorial(x - 1) % DIV


def square(x, n):
    if n == 0:
        return 0
    if n == 1:
        return x % DIV

    y = square(x, n // 2)
    if n % 2 == 0:
        return y * y % DIV
    else:
        return y * y * x % DIV


N, K = map(int, input().split())
DIV = 1000000007
top = factorial(N)
bottom = factorial(N-K) * factorial(K) % DIV
result = top * square(bottom, DIV - 2) % DIV
print(result)