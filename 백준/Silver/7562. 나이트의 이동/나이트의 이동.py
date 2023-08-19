def bfs(N, x, y):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append(x)
    visited[x[0]][x[1]] = 0
    move = [(-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)]  # 나이트의 이동 범위

    while q:
        i, j = q.popleft()
        for k in move:
            ni, nj = i+k[0], j+k[1]
            # 나이트의 이동 범위가 체스판 내부이고 방문하지 않았다면
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==-1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
            # 도착 지점이라면
            if [ni, nj] == y:
                return visited[ni][nj]


from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())    # 체스판 한 변의 길이
    x = list(map(int, input().split()))     # 현재 위치
    y = list(map(int, input().split()))     # 이동할 위치
    print(bfs(N, x, y))