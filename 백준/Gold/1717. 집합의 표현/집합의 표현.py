import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(res, x, y):
    x = find_set(x)
    y = find_set(y)

    if res: # 합집합
        if x == y:
            print('YES')
        else:
            print('NO')

    else:   # 유니온
        if x < y:
            parent[y] = x
        else:
            parent[x] = y


N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
connected = []

for _ in range(M):
    res, e1, e2 = map(int, input().split())
    union(res, e1, e2)