def f(i, N, M):
    if i == M:
        print(*path)
        return

    for j in range(1, N+1):
        if j in path:
            continue
        path[i] = j
        f(i + 1, N, M)
        path[i] = 0


N, M = map(int, input().split())
path = [0] * M
f(0, N, M)