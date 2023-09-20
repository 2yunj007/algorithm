def f(i, N, M):
    if i == M:
        print(*path)
        return

    for j in range(1, N+1):
        if path[i] == 1:
            continue
        if i > 0 and j < path[i - 1]:
            continue
        path[i] = j
        f(i + 1, N, M)
        path[i] = 0


N, M = map(int, input().split())
path = [0] * M
f(0, N, M)