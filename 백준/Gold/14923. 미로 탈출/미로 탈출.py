from collections import deque
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
Hx, Hy = map(int, input().split())  # 시작
Ex, Ey = map(int, input().split())  # 끝
arr = [list(map(int, input().split())) for _ in range(N)]   # 0: 길, 1: 벽

q = deque([(Hx - 1, Hy - 1, 0, 0)])
visited = [[[False] * M for _ in range(N)] for _ in range(2)]
visited[0][0][0] = 0
D = ((-1, 0), (1, 0), (0, -1), (0, 1))

while q:
    i, j, cnt, is_break = q.popleft()
    if i == Ex - 1 and j == Ey - 1:
        print(cnt)
        exit()
    for d in D:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[is_break][ni][nj]:
                continue
            if arr[ni][nj] and not is_break:
                q.append((ni, nj, cnt + 1, 1))
                visited[is_break][ni][nj] = True
            elif not arr[ni][nj]:
                q.append((ni, nj, cnt + 1, is_break))
                visited[is_break][ni][nj] = True
print(-1)