import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parent[y] = x
        cnt[x] += cnt[y]
    else:
        parent[x] = y
        cnt[y] += cnt[x]


N = int(input())
for _ in range(N):
    M = int(input())

    parent = {}
    cnt = {}
    for m in range(M):
        p1, p2 = input().split()
        if p1 not in parent:
            parent[p1] = p1
            cnt[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            cnt[p2] = 1

        union(p1, p2)
        print(cnt[find_set(p1)])