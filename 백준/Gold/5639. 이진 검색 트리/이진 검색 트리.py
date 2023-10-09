import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def postorder(start, end):
    if start > end:
        return

    root = preorder[start]

    # tmp = 0
    tmp = end + 1   # 모든 원소가 루트 노드보다 작은 경우를 대비

    for i in range(start, end + 1):
        # 루트보다 큰 값이 나오면 분할
        if preorder[i] > root:
            tmp = i
            break

    postorder(start + 1, tmp - 1)
    postorder(tmp, end)
    print(root)


preorder = []
while True:
    try: preorder.append(int(input()))
    except: break

postorder(0, len(preorder) - 1)