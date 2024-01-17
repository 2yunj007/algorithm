T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    N = len(W)

    cnt = {}
    for i in range(N):
        cnt.setdefault(W[i], 0)
        cnt[W[i]] += 1

    location = {}
    for i in range(N):
        if cnt[W[i]] >= K:
            location.setdefault(W[i], [])
            location[W[i]].append(i)

    max_len, min_len = 0, 10001
    for s in location:
        max_len = max([max_len] + [location[s][j + K - 1] - location[s][j] + 1 for j in range(len(location[s]) - K + 1)])
        min_len = min([min_len] + [location[s][j + K - 1] - location[s][j] + 1 for j in range(len(location[s]) - K + 1)])

    if max_len == 0:
        print(-1)
    else:
        print(min_len, max_len)