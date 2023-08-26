T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    min_change = N*M

    # 0~w 행은 흰색, w~b행은 파란색, 그 이후는 빨간색
    # 위 규칙으로 칠하기 위해 b와 r을 결정함
    for w in range(N-2):
        for b in range(w+1, N-1):
            cnt = 0
            for i in range(N):
                for j in range(M):
                    # 흰색 부분
                    if i <= w and arr[i][j] != 'W':
                        cnt += 1
                    # 파란색 부분
                    if w < i <= b and arr[i][j] != 'B':
                        cnt += 1
                    # 빨간색 부분
                    if b < i and arr[i][j] != 'R':
                        cnt += 1
            min_change = min(min_change, cnt)

    print(f'#{tc} {min_change}')