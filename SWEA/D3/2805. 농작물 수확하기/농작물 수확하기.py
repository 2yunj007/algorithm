T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    rst = 0     # 수익

    n = 1   # 마름모의 각 행에 대한 열의 크기
    j = N // 2  # 마름모의 각 행에서 수확을 시작하는 열 번호
    for r in range(N):
        if 0 < r <= N//2:   # 행이 마름모의 위쪽 영역일 경우
            n += 2
            j -= 1
        elif r > N//2:      # 행이 마름모의 아래쪽 영역일 경우
            n -= 2
            j += 1
        for c in range(j, j+n):
            rst += arr[r][c]

    print(f'#{tc} {rst}')