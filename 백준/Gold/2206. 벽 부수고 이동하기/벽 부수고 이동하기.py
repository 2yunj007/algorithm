from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    global N, M
    # 벽을 부수지 않았을 때와 부수었을 때의 경우를 구분하여 방문 여부 저장
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))  # row, col, 벽 파괴 여부
    visited[0][0][0] = 1

    while q:
        i, j, broken = q.popleft()

        if i == N - 1 and j == M - 1:  # 도착 지점에 도달한 경우
            return visited[i][j][broken]

        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
            ni, nj = i + d[0], j + d[1]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][broken]:
                if not arr[ni][nj]:     # 벽이 없다면 이동
                    visited[ni][nj][broken] = visited[i][j][broken] + 1
                    q.append((ni, nj, broken))
                elif not broken:  # 벽을 만났는데, 아직 한 번도 부수지 않았다면
                    visited[ni][nj][1] = visited[i][j][0] + 1
                    q.append((ni, nj, 1))  # 벽을 부수고 이동

    return -1  # 도착 지점에 도달하지 못한 경우


N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

print(bfs())