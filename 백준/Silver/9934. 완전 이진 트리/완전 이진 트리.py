import sys
input = sys.stdin.readline


def make_tree(lst, depth):
    mid = len(lst) // 2
    tree[depth].append(lst[mid])
    if len(lst) == 1:
        return
    make_tree(lst[:mid], depth + 1)
    make_tree(lst[mid+1:], depth + 1)

    
K = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(K)]
make_tree(arr, 0)

for i in range(K):
    print(*tree[i])