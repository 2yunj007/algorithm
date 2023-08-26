# 왼쪽 위 모서리부터 bfs로 탐색을 시작하면
# 오른쪽 아래 모서리를 제일 나중에 탐색하게 됨
def bfs(row, col):
    q = [(row, col)]
    visited[row][col] = 1
    while True:
        i, j = q.pop(0)
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:    # 상하좌우 탐색
            ni, nj = i+d[0], j+d[1]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
        if not q:   # 마지막 원소를 디큐했는데 더 이상 탐색할 수 없는 경우
            return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cnt = 0     # 행렬 수
    size = []   # 행렬 크기

    for r1 in range(N):
        for c1 in range(N):
            # 행렬의 시작점을 찾음
            if arr[r1][c1] and not visited[r1][c1]:
                cnt += 1
                r2, c2 = bfs(r1, c1)
                r = r2 - r1 + 1
                c = c2 - c1 + 1
                size.append((r*c, r, c))    # 행렬 크기, 행, 열

    print(f'#{tc} {cnt}', end=' ')

    size.sort()     # 첫 번째 원소인 크기를 기준으로 정렬됨, 같다면 두 번째 원소로
    for s, r, c in size:
        print(r, c, end=' ')
    print()