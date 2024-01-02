import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def make_tree(start, end, i):
    # 리프 노드에 도달하면 값 삽입
    if start == end:
        tree[i][0], tree[i][1] = arr[start], arr[start]
        return tree[i]

    mid = (start + end) // 2
    # 좌측 서브 트리와 우측 서브 트리 값을 채우면서 부모 노드도 채움
    left = make_tree(start, mid, i*2)
    right = make_tree(mid+1, end, i*2+1)
    tree[i][0] = min(left[0], right[0])     # 구간 최솟값
    tree[i][1] = max(left[1], right[1])     # 구간 최댓값
    return tree[i]


def find_min_max(start, end, a, b, i):
    # 범위를 벗어날 경우
    if a > end or b < start:
        return (10**9, 0)

    # start~end에 a~b가 포함되어 있는 경우
    if a <= start and b >= end:
        return tree[i]

    mid = (start + end) // 2
    left = find_min_max(start, mid, a, b, i*2)
    right = find_min_max(mid+1, end, a, b, i*2+1)
    min_ = min(left[0], right[0])
    max_ = max(left[1], right[1])
    return min_, max_


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# N보다 크면서 가장 가까운 N의 제곱수 * 2의 크기의 트리 배열이 필요
# 넉넉하게 N*4라고 생각
# [구간의 최솟값, 최댓값]
tree = [[0, 0] for _ in range(N*4)]

make_tree(0, N - 1, 1)
# print(tree)

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(*find_min_max(0, N - 1, a, b, 1))