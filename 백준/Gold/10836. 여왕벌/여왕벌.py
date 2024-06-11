import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [[1] * M for _ in range(M)]
add = [[1] * M for _ in range(M)]

for _ in range(N):
    init = list(map(int, input().split()))

    i = M - 1
    j = 0
    n = 0

    # 첫 번째 열/행에 대한 초깃값 설정
    while j < M:
        while True:
            if init[n]:
                break
            else:
                n += 1

        init[n] -= 1
        add[i][j] = n
        arr[i][j] += add[i][j]

        if i > 0:
            i -= 1
        else:
            j += 1

    # 왼쪽, 왼쪽 위, 위쪽 중 자라는 정도는 무조건 위쪽 (초기 입력에서의 감소하지 않는 형태라는 조건 때문)
    # r = 1에 대해서만 연산한 뒤 마지막에 반영
    for c in range(1, M):
        add[1][c] = add[1 - 1][c]
        arr[1][c] += add[1][c]

for r in range(2, M):
    for c in range(1, M):
        arr[r][c] = arr[1][c]

for i in range(0, M):
    print(*arr[i])