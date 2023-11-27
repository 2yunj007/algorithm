from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj):
    q = deque()
    visit[si][sj] = 1
    q.append((si, sj))
    cnt_lst = []

    while q:
        i, j = q.popleft()
        cnt = 0
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + d[0], j + d[1]

            if not(0 <= ni < N and 0 <= nj < M):
                continue
            if visit[ni][nj]:
                continue
            # 바다 개수 카운트
            if not arr[ni][nj]:
                cnt += 1
                continue

            q.append((ni, nj))
            visit[ni][nj] = 1

        # 녹일 빙산 리스트에 저장
        if cnt:
            cnt_lst.append((i, j, cnt))

    # 빙산 녹이기, 0보다 작으면 0으로
    for i, j, cnt in cnt_lst:
        arr[i][j] = max(0, arr[i][j] - cnt)

    return 1


N, M = map(int, input().split())    # r c
arr = [list(map(int, input().split())) for _ in range(N)]

# 빙산 위치 저장
ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ice.append((i, j))

year = 0
while ice:
    visit = [[0] * M for _ in range(N)]
    melt_lst = []
    n = 0
    for i, j in ice:
        if arr[i][j] and not visit[i][j]:
            n += bfs(i, j)
        # 다 녹았으면 리스트에 저장
        if not arr[i][j]:
            melt_lst.append((i, j))
    # 빙산 그룹이 2개 이상일 경우
    if n > 1:
        print(year)
        exit()
    # 다 녹은 빙산 삭제 후 반복
    ice = sorted(list(set(ice) - set(melt_lst)))
    year += 1

if n < 2: print(0)