T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0

    for r in range(N):
        for c in range(N):
            sum_t = arr[r][c]
            sum_x = arr[r][c]
            for m in range(1, M):
                for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = r+i[0]*m, c+i[1]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_t += arr[ni][nj]
                for j in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:
                    ni, nj = r+j[0]*m, c+j[1]*m
                    if 0 <= ni < N and 0 <= nj < N:
                        sum_x += arr[ni][nj]
            max_fly = max(sum_t, sum_x, max_fly)

    print(f'#{tc} {max_fly}')