from math import sqrt
import sys
input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def distance(a, b):
    return sqrt((coor[a][0] - coor[b][0]) ** 2 + (coor[a][1] - coor[b][1]) ** 2)


V = int(input())
edge = []
coor = [list(map(float, input().split())) for _ in range(V)]

for i in range(V):
    for j in range(i + 1, V):
        edge.append([i, j, distance(i, j)])

# 거리를 기준으로 정렬
edge.sort(key=lambda x: x[2])

parents = [i for i in range(V)]

sum_distance = 0
for f, t, d in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        union(f, t)
        sum_distance += d

print(round(sum_distance, 2))