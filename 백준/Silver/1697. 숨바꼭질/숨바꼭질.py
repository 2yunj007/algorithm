def bfs(N, K):
    visited = {}    # 방문 여부를 확인할 때 시간 복잡도를 줄이기 위함
    q = deque()     # pop(0) -> 시간 초과
    q.append(N)     # 시작 정점 인큐
    visited[N] = 0  # 시작 정점 방문 표시

    while q:
        X = q.popleft()
        for w in [X-1, X+1, X*2]:
            # 아직 방문하지 않았다면 인큐 및 방문 표시
            # w 범위에 대한 조건이 없으면 메모리 초과
            if 0 <= w < 10**6 and w not in visited:
                q.append(w)
                visited[w] = visited[X] + 1
            # 동생을 찾았다면 찾은 시간 반환
            if w == K:
                return visited[w]


from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
print(bfs(N, K))
