import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(now):
    global ans

    visited[now] = True
    cycle.append(now)

    next = arr[now]

    if visited[next]:
        # 사이클 발생
        if next in cycle:
            ans -= len(cycle[cycle.index(next):])
            return
    else:
        dfs(next)


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    ans = N

    for i in range(1, N + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(ans)