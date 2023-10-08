import sys
sys.setrecursionlimit(10**9)    # RecursionError
input = sys.stdin.readline


# 후위 순회를 했을 때 마지막으로 방문하는 노드는 해당 트리의 루트 노드
# 중위 순회를 했을 때 루트 노드를 기준으로 왼쪽, 오른쪽 서브 트리로 나뉨
def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=' ')  # 루트 출력

    left = root_idx[root] - in_start
    right = in_end - root_idx[root]

    # 왼쪽 서브트리
    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른쪽 서브트리
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

root_idx = [0] * (N + 1)
for i in range(N):
    root_idx[inorder[i]] = i

preorder(0, N - 1, 0, N - 1)