import sys
input = sys.stdin.readline

# 첫 번째 열/행 제외하고는 모두 위쪽 값과 동일함

M, N = map(int, input().split())
grow = [1] * (M*2 - 1)

for _ in range(N):
    a, b, c = list(map(int, input().split()))

    for i in range(a, a + b):
        grow[i] += 1

    for i in range(a + b, M*2 - 1):
        grow[i] += 2

for r in range(M - 1, -1, -1):
    print(*([grow[r]] + grow[M:]))