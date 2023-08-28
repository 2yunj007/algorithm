from collections import deque
M, N, H = map(int, input().split())    # 상자의 가로/세로 칸 수
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]   # 토마토 상태
ripe = []   # 초반의 익은 토마토 리스트
queue = deque()
day = 0

for h in range(H):
    for r in range(N):
        for c in range(M):
            # 익은 토마토의 좌표 저장해 두기
            if arr[h][r][c] == 1:
                ripe.append((h, r, c))

for h, r, c in ripe:   # bfs
    # 익은 토마토 모두 인큐
    queue.append((h, r, c))

while queue:
    h, r, c = queue.popleft()
    for d in [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (1,0,0), (-1,0,0)]:
        nh, ni, nj = h+d[0], r+d[1], c+d[2]
        # 상자 내부이며 익지 않은 토마토일 경우
        if 0<=nh<H and 0<=ni<N and 0<=nj<M and arr[nh][ni][nj]==0:
            queue.append((nh, ni, nj))  # 인큐
            arr[nh][ni][nj] = arr[h][r][c] + 1     # 토마토 익음 표시
    # 탐색이 끝났으면 마지막 방문 수 받음
    if not queue:
        day = arr[h][r][c] - 1

# 익지 않은 토마토가 있으면 -1 출력 후 종료
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 0:
                print(-1)
                exit()
print(day)