import sys
input = sys.stdin.readline

# 깊이우선탐색, DFS
# 스택에서 빼면서 방문
def dfs(V, S):
    visited = [0]*(V+1)
    s = [S]
    cnt = 0
    while s:
        t = s.pop()
        if visited[t] == 0:
            cnt += 1
            visited[t] = cnt
            for w in adj_l[t][::-1]:
                if visited[w] == 0:
                    s.append(w)
    # 1부터 마지막으로 방문한 순서(visited의 최댓값)까지 순회하며
    # 그에 해당하는 인덱스(노드 번호) 출력
    for i in range(1, max(visited)+1):
        print(visited.index(i), end=' ')

# 너비우선탐색, BFS
# 큐에 넣으면서 방문
def bfs(V, S):
    visited = [0]*(V+1)
    q = [S]
    visited[S] = 1
    cnt = 1
    while q:
        t = q.pop(0)
        for w in adj_l[t]:
            if visited[w] == 0:
                cnt += 1
                visited[w] = cnt
                q.append(w)

    for i in range(1, max(visited)+1):
        print(visited.index(i), end=' ')


V, E, S = map(int, input().split())
adj_l = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
for i in adj_l:
    i.sort()
dfs(V, S)
print()
bfs(V, S)