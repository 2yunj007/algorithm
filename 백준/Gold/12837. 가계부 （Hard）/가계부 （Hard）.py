import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def find(start, end, p, q, i):
    if p > end or q < start:
        return 0

    if p <= start and q >= end:
        return tree[i]

    mid = (start + end) // 2
    left = find(start, mid, p, q, i*2)
    right = find(mid+1, end, p, q, i*2+1)
    return left + right


def update(start, end, p, x, i):
    if p < start or p > end:
        return tree[i]

    if start == end:
        tree[i] += x
        return tree[i]

    mid = (start + end) // 2
    left = update(start, mid, p, x, i*2)
    right = update(mid+1, end, p, x, i*2+1)
    tree[i] = left + right
    return tree[i]


N, Q = map(int, input().split())

tree = [0] * (N*4)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        update(0, N-1, query[1]-1, query[2], 1)
    elif query[0] == 2:
        print(find(0, N-1, query[1]-1, query[2]-1, 1))