import sys
input = sys.stdin.readline


def mul(arr1, arr2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k] * arr2[k][j] % DIV
            result[i][j] %= DIV
    return result


def square(arr, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                arr[i][j] %= DIV
        return arr

    tmp = square(arr, n // 2)
    if n % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), arr)


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DIV = 1000
result = square(arr, B)
for i in range(N):
    print(*result[i])