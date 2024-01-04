import sys, heapq
input = sys.stdin.readline

# 너비가 넓은 길부터 꺼내어 (최대힙) 유니온-파인드
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


p, w = map(int, input().split())
world_B, world_C = map(int, input().split())

arr = []
for _ in range(w):
    start, end, width = map(int, input().split())
    heapq.heappush(arr, (-width, start, end))

parent = list(range(p))
answer = 0

while arr:
    width, start, end = heapq.heappop(arr)
    width = -width
    union(start, end)

    if find(world_B) == find(world_C):
        answer = width
        break

print(answer)

# 시간 초과
# p, w = map(int, input().split())
# world_B, world_C = map(int, input().split())
# arr = [[0] * p for _ in range(p)]
# visited = [0] * p
# answer = 0
#
# for _ in range(w):
#     start, end, width = map(int, input().split())
#     arr[start][end] = width
#     arr[end][start] = width
#
#
# def dfs(now, min_):
#     global answer
#     if min_ <= answer:
#         return
#
#     if now == world_C:
#         answer = min_
#
#     for next in range(p):
#         if arr[now][next] and not visited[next]:
#             visited[next] = 1
#             dfs(next, min(min_, arr[now][next]))
#             visited[next] = 0
#
#
# visited[world_B] = 1
# dfs(world_B, 50000)
# print(answer)