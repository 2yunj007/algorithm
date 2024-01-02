import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def make_tree(start, end, i):
    if start == end:
        tree[i] = arr[start]
        return tree[i]

    mid = (start + end) // 2
    left = make_tree(start, mid, i*2)
    right = make_tree(mid+1, end, i*2+1)
    tree[i] = left + right
    return tree[i]


def find_sum(start, end, x, y, i):
    if x > end or y < start:
        return 0

    if x <= start and y >= end:
        return tree[i]

    mid = (start + end) // 2
    left = find_sum(start, mid, x, y, i*2)
    right = find_sum(mid+1, end, x, y, i*2+1)
    return left + right


def update(start, end, a, b, i):
    if a < start or a > end:
        return tree[i]

    if start == end:
        tree[i] = b
        return tree[i]

    mid = (start + end) // 2
    left = update(start, mid, a, b, i*2)
    right = update(mid+1, end, a, b, i*2+1)
    tree[i] = left + right
    return tree[i]


N, Q = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (N * 4)
make_tree(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(find_sum(0, N-1, x-1, y-1, 1))
    update(0, N-1, a-1, b, 1)