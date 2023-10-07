import sys
input = sys.stdin.readline


def preorder(node):
    if node:
        # 루트 출력
        print(node, end='')
        # 왼쪽 서브 트리 순회
        preorder(graph[node][0])
        # 오른쪽 서브 트리 순회
        preorder(graph[node][1])


def inorder(node):
    if node:
        # 왼쪽 서브 트리 순회
        inorder(graph[node][0])
        # 루트 출력
        print(node, end='')
        # 오른쪽 서브 트리 순회
        inorder(graph[node][1])


def postorder(node):
    if node:
        # 왼쪽 서브 트리 순회
        postorder(graph[node][0])
        # 오른쪽 서브 트리 순회
        postorder(graph[node][1])
        # 루트 출력
        print(node, end='')


N = int(input())
graph = {}
for i in range(N):
    parents, child1, child2 = input().split()
    graph.setdefault(parents, ['', ''])
    if child1 != '.':
        graph[parents][0] = child1
    if child2 != '.':
        graph[parents][1] = child2

preorder('A')
print()
inorder('A')
print()
postorder('A')