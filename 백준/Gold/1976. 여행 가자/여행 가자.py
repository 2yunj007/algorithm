import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
M = int(input())

# 2차원 배열 그래프
graph = [list(map(int, input().split())) for _ in range(N)]
# 여행 계획 (M개)
plan = list(map(int, input().split()))
# 대표자
parent = [i for i in range(N)]

# 유니온
for i in range(N):
    for j in range(N):
        if graph[i][j]:  # 연결된 도시
            union(i, j)

# 대표자 갱신
for i in range(N):
    find_set(parent[i])

# 방문 계획 도시들이 모두 같은 집합인지 확인
for i in range(1, M):
    if parent[plan[i - 1] - 1] != parent[plan[i] - 1]:
        print('NO')
        break
else:
    print('YES')