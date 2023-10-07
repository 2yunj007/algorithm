import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    max_weight = [0, 0]
    visited = [-1] * (10001)
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.popleft()
        for next, weight in graph[now]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + weight
                if visited[next] > max_weight[0]:
                    max_weight[0] = visited[next]
                    max_weight[1] = next

    return max_weight


n = int(input())
graph = [[] for _ in range(10001)]
for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

depth, node = bfs(1)
depth, node = bfs(node)
print(depth)