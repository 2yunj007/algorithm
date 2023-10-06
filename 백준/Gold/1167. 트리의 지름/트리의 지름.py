import sys
input = sys.stdin.readline
from collections import deque

# bfs로 첫 번째 노드에서 제일 먼 노드의 번호를 찾음
# 제일 먼 노드의 번호부터 다시 탐색하여 제일 먼 노드를 찾음
def bfs(start):
    max_depth = [0, 0]
    visited = [-1] * (V + 1)
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        now = q.popleft()
        for next, depth in graph[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + depth
                if visited[next] > max_depth[0]:
                    max_depth[0] = visited[next]
                    max_depth[1] = next
    return max_depth


V = int(input())
graph = [[] for _ in range(V + 1)]

for i in range(V):
    lst = list(map(int, input().split()))

    for j in range(1, len(lst) - 2, 2):
        graph[lst[0]].append((lst[j], lst[j + 1]))

depth, node = bfs(1)
depth, node = bfs(node)
print(depth)