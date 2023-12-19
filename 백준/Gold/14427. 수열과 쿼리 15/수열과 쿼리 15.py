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

    if left[1] < right[1]:
        tree[i] = left
    elif right[1] < left[1]:
        tree[i] = right
    elif left[0] < right[0]:
        tree[i] = left
    elif left[0] > right[0]:
        tree[i] = right
    return tree[i]


def find_min(start, end, x, y, i):
    if x > end or y < start:
        return 10**5+1, 10**9+1

    if x <= start and y >= end:
        return tree[i]

    mid = (start + end) // 2
    left = find_min(start, mid, x, y, i*2)
    right = find_min(mid+1, end, x, y, i*2+1)

    if left[1] < right[1]:
        tree[i] = left
    elif right[1] < left[1]:
        tree[i] = right
    elif left[0] < right[0]:
        tree[i] = left
    elif left[0] > right[0]:
        tree[i] = right
    return tree[i]


def update(start, end, a, b, i):
    if a < start or a > end:
        return tree[i]

    if start == end:
        tree[i] = (a, b)
        return tree[i]

    mid = (start + end) // 2
    left = update(start, mid, a, b, i*2)
    right = update(mid+1, end, a, b, i*2+1)

    if left[1] < right[1]:
        tree[i] = left
    elif right[1] < left[1]:
        tree[i] = right
    elif left[0] < right[0]:
        tree[i] = left
    elif left[0] > right[0]:
        tree[i] = right
    return tree[i]


N = int(input())
arr = list(enumerate(map(int, input().split())))
M = int(input())

tree = [(0, 0) for _ in range(N*4)]
make_tree(0, N-1, 1)

for _ in range(M):
    query = list(map(int, input().split()))
    if len(query) != 1:
        update(0, N-1, query[1]-1, query[2], 1)
    else:
        print(find_min(0, N-1, 0, N-1, 1)[0]+1)
