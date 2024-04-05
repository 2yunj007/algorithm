from math import trunc
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0

visited = [[False] * N for _ in range(N)]
D = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상
d = 0       # 현재 방향
drt = 1     # 중심으로부터의 거리
sr, sc = N//2, N//2   # 시작 위치 (중심)

# 방향에 따라 모래가 퍼지는 비율
spread = {
    0.1: [
        [(-1, -1), (1, -1)],
        [(1, -1), (1, 1)],
        [(1, 1), (-1, 1)],
        [(-1, 1), (-1, -1)]
    ],
    0.07: [
        [(-1, 0), (1, 0)],
        [(0, -1), (0, 1)],
        [(-1, 0), (1, 0)],
        [(0, -1), (0, 1)]
    ],
    0.05: [
        [(0, -2)],
        [(2, 0)],
        [(0, 2)],
        [(-2, 0)]
    ],
    0.02: [
        [(-2, 0), (2, 0)],
        [(0, -2), (0, 2)],
        [(-2, 0), (2, 0)],
        [(0, -2), (0, 2)]
    ],
    0.01: [
        [(1, 1), (-1, 1)],
        [(-1, 1), (-1, -1)],
        [(-1, -1), (1, -1)],
        [(1, -1), (1, 1)],
    ],
}

r, c = sr, sc
visited[sr][sc] = True

while True:
    nr, nc = r + D[d][0], c + D[d][1]

    # 현재 이동할 위치의 중심으로부터의 거리가 drt인지 확인
    if (nr, nc) == (sr - drt, sc - drt):
        drt += 1
    else:
        if not(abs(sr - nr) <= drt and abs(sc - nc) <= drt):
            # drt에서 벗어날 경우 방향 전환
            d = (d + 1) % 4
            continue

    # 범위를 벗어나거나 방문한 곳일 경우 drt++
    if not(0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
        drt += 1
        continue

    r, c = nr, nc
    visited[nr][nc] = True
    sand = arr[r][c]

    if sand:
        # 모래 확산
        for s in spread:
            for p in spread[s][d]:
                pr, pc = r + p[0], c + p[1]
                add_sand = int(trunc(sand * s))
                arr[r][c] -= add_sand

                # 모래가 퍼질 위치가 범위를 벗어나는 경우
                if 0 <= pr < N and 0 <= pc < N:
                    arr[pr][pc] += add_sand
                else:
                    answer += add_sand

        if 0 <= r + D[d][0] < N and 0 <= c + D[d][1] < N:
            arr[r + D[d][0]][c + D[d][1]] += arr[r][c]
            arr[r][c] = 0
        else:
            answer += arr[r][c]

        arr[r][c] = 0

    # 도착점
    if (r, c) == (0, 0):
        break

print(answer)