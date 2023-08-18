import sys
input = sys.stdin.readline


def bfs(N, R):
    visited = [0]*(N+1)
    q = [R]
    visited[R] = 1  # 시작 정점 방문 순서
    cnt = 1     # 방문 카운트
    while q:
        t = q.pop(0)    # 방문할 노드 디큐
        for w in adj_l[t]:
            if visited[w] == 0:     # 아직 방문하지 않았으면
                q.append(w)     # 인큐
                cnt += 1    # 방문 횟수 증가
                visited[w] = cnt
    return visited


N, M, R = map(int, input().split())     # 정점/간선/시작정점
# 간선 정보를 담을 리스트 생성
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)    # 무방향 그래프
    adj_l[v2].append(v1)
# 오름차순으로 방문하기 위해 정렬
for i in range(N+1):
    adj_l[i].sort(reverse=True)
# 출력
for i in bfs(N, R)[1:]:
    print(i)