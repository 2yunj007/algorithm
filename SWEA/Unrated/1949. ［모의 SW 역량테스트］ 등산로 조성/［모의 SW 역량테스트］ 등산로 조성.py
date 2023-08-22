# 봉우리에서 가장 긴 길을 찾는 함수 : DFS 사용
def count_load(i, j, cnt):
    global len_load, N
    # 지금까지 저장된 경로보다 길다면 최댓값 재할당
    if cnt > len_load:
        len_load = cnt
    # 해당 칸에 대해 인접한 모든 칸 탐색
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:    # 상하좌우
        ni, nj = i+d[0], j+d[1]
        # 인접한 칸이 배열 범위를 벗어나지 않고, 이전에 방문한 값보다 작고, 미방문 상태라면
        # 해당 칸을 방문 표시하고 그 인접한 칸으로 넘어감
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] < arr[i][j] and not visited[ni][nj]:
            visited[i][j] = True  # 방문 표시
            count_load(ni, nj, cnt+1)   # 인접한 칸에 대해서 다시 길을 찾음
            visited[i][j] = False # 방문 해제
            # 길의 끝까지 방문한 후
            # 다른 경로에서 길이 중복되어 미방문 하는 것을 방지하기 위해 방문 해제함

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 지도 한 변의 길이, 산 깎는 값
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    b = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > b:
                b = arr[r][c]

    # 봉우리 리스트 생성
    b_lst = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == b:
                b_lst.append((r, c))

    len_load = 0    # 등산로의 길이를 카운트할 변수
    visited = [[False] * N for _ in range(N)]

    # 배열을 순회하면서
    for r in range(N):
        for c in range(N):
            for k in range(1, K+1):
                arr[r][c] -= k  # 해당 칸에서 K를 빼고
                for i, j in b_lst:     # 각각의 봉우리에 대해 가장 긴 길을 찾아 봄
                    count_load(i, j, 1)
                arr[r][c] += k  # K를 다시 더하여 배열을 초기 상태로 돌림

    print(f'#{tc} {len_load}')