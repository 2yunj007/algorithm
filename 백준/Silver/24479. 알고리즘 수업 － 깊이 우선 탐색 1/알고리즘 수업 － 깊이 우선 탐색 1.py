import sys
input = sys.stdin.readline

N, M, R = map(int, input().split()) # 정점 수, 간선 수, 시작 정점
lst = [[] for _ in range(N+1)]
# [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]
for i in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

# 내림차순으로 정렬해야 스택에 전부 넣고 다시 pop 할 때 오름차순으로 빠짐
for i in range(N+1):
    lst[i].sort(reverse=True)

stack = [R]
visited = [0]*(N+1)     # 방문 여부 및 순서
cnt = 1     # 방문 순서 카운트

# 스택에서 더 이상 꺼낼 노드가 없으면 종료
while stack:
    node = stack.pop()
    # 방문한 노드라면 수행하지 않고 넘어감
    if visited[node] != 0:
        continue

    # 방문하지 않은 노드라면 방문 여부 표시
    visited[node] = cnt
    cnt += 1

    # 해당 노드와 연결된 다른 노드가 방문 이력이 없으면 스택에 삽입
    for i in lst[node]:
        if visited[i] == 0:
            stack.append(i)

print(*visited[1:], sep='\n')