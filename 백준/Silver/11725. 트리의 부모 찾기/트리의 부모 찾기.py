import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

while queue:
    tmp = queue.popleft()
    for n in graph[tmp]:
        if parents[n]:
            continue
        parents[n] = tmp
        queue.append(n)

for i in range(2, N + 1):
    print(parents[i])
