from collections import deque

def solution(n, roads, sources, destination):
    # 방문을 못 할 경우 -1로 남아 있음
    visited = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    # 도착 지점에서 시작
    q = deque([destination])
    visited[destination] = 0
    while q:
        now = q.popleft()

        for node in graph[now]:
            # 아직 방문하지 않았으면
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                q.append(node)

    return [visited[i] for i in sources]