import sys
input = sys.stdin.readline


def dfs(r, c):
    # 오른쪽 끝에 도착하면 1 카운트
    if r == N - 1 and c == M - 1:
        return 1

    # 이미 방문했던 곳이라면
    # 이미 거기서부터 오른쪽 끝까지 가는 경우의 수가 저장되어 있을 거임
    # 더 가지 않고 저장된 값 리턴
    if dp[r][c] != -1:
        return dp[r][c]

    cnt = 0
    # 상하좌우로 갔을 때 각각의 경우의 수 카운트
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] < arr[r][c]:
                cnt += dfs(nr, nc)

    dp[r][c] = cnt
    return dp[r][c]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
print(dfs(0, 0))