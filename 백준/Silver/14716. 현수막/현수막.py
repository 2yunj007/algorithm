import sys
from collections import deque
import sys


def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 0

    while q:
        si, sj = q.popleft()

        for d in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = si + d[0], sj + d[1]
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj]:
                q.append((ni, nj))
                arr[ni][nj] = 0


input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
answer = 0

for i in range(M):
    for j in range(N):
        if arr[i][j]:
            bfs(i, j)
            answer += 1

print(answer)