import sys
input = sys.stdin.readline


def f(x, n, c):
    if n == 1:
        return x % c
    if n % 2 == 0:  # 지수가 짝수
        y = f(x, n//2, c)
        return y * y % c
    else:   # 지수가 홀수
        y = f(x, n//2, c)
        return y * y * x % c


x, n, c = map(int, input().split())
print(f(x, n, c))