def f(cnt):
    global answer

    # 핀 위치
    pins = []
    for r in range(5):
        for c in range(9):
            if arr[r][c] == 'o':
                pins.append((r, c))

    # 최소 개수, 이동 횟수 갱신
    if len(pins) < answer[0]:
        answer[0] = len(pins)
        answer[1] = cnt
    elif len(pins) == answer[0]:
        answer[1] = min(answer[1], cnt)

    # 핀 이동
    for r, c in pins:
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < 5 and 0 <= nc < 9 and arr[nr][nc] == 'o':
                nnr, nnc = nr + d[0], nc + d[1]
                if 0 <= nnr < 5 and 0 <= nnc < 9 and arr[nnr][nnc] == '.':
                    arr[r][c] = '.'
                    arr[nr][nc] = '.'
                    arr[nnr][nnc] = 'o'
                    f(cnt + 1)
                    # 복귀
                    arr[r][c] = 'o'
                    arr[nr][nc] = 'o'
                    arr[nnr][nnc] = '.'


T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    if tc < T:
        input()
    answer = [8, 8]
    f(0)
    print(*answer)