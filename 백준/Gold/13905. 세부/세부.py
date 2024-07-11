import sys
import heapq
INF = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
answer = 0
distance = [0] * (N+1)

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2].append((h1, k))

h = []
heapq.heappush(h, (-INF, s))
distance[s] = INF

while h:
    dist, now = heapq.heappop(h)
    dist = - dist
    if distance[now] > dist:
        continue
    for node, d in edges[now]:
        cost = min(dist, d)
        if cost > distance[node]:
            distance[node] = cost
            heapq.heappush(h, (-cost, node))

print(distance[e])