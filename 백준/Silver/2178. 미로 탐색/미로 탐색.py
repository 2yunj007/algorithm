def bfs(N, M):
    visited = [[0]*M for _ in range(N)]
    q = [[0, 0]]        # 시작 정점 인큐
    visited[0][0] = 1   # 시작 정점 방문 표시

    while q:
        i, j = q.pop(0)
        for k in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i+k[0], j+k[1]
            # 길이 존재하며 방문하지 않았을 경우
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visited[ni][nj]==0:
                q.append([ni, nj])  # 인큐
                visited[ni][nj] = visited[i][j] + 1  # 방문 순서 증가
                # 도착 노드라면 방문 순서 리턴
                if ni==N-1 and nj==M-1:
                    return visited[ni][nj]
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list((map(int, input().strip()))) for _ in range(N)]
print(bfs(N, M))