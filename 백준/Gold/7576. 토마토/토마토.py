from collections import deque
M, N = map(int, input().split())    # 상자의 가로/세로 칸 수
arr = [list(map(int, input().split())) for _ in range(N)]   # 토마토 상태
ripe = []   # 초반의 익은 토마토 리스트
queue = deque()
day = 0

for r in range(N):
    for c in range(M):
        # 익은 토마토의 좌표 저장해 두기
        if arr[r][c] == 1:
            ripe.append((r, c))

for r, c in ripe:   # bfs
    # 익은 토마토 모두 인큐
    queue.append((r, c))

while queue:
    i, j = queue.popleft()
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i+d[0], j+d[1]
        # 상자 내부이며 익지 않은 토마토일 경우
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
            queue.append((ni, nj))  # 인큐
            arr[ni][nj] = arr[i][j] + 1     # 토마토 익음 표시
    # 탐색이 끝났으면 마지막 방문 수 받음
    if not queue:
        day = arr[i][j] - 1

# 익지 않은 토마토가 있으면 -1 출력 후 종료
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            print(-1)
            exit()
print(day)