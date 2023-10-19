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
        return False

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return True


N, M = map(int, input().split())
parent = [i for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    if not union(x, y):
        print(i + 1)
        exit()
print(0)