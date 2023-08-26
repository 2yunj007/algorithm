for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_d = 10000   # 최단 거리
    x = 0   # 최단 거리를 가지는 시작점

    for i in range(100):
        if arr[0][i] == 1:  # 출발 지점 찾음
            r = 0
            c = i
            d = 0   # 거리
            visited = [[0] * 100 for _ in range(100)]  # 방문 표시 배열
            while r != 99:   # 바닥에 도착할 때까지 반복
                visited[r][c] = 1
                d += 1
                #  오른쪽으로 이동
                if c+1 < 100 and arr[r][c+1] == 1 and visited[r][c+1] == 0:
                    c += 1
                # 왼쪽으로 이동
                elif c-1 >= 0 and arr[r][c-1] == 1 and visited[r][c-1] == 0:
                    c -= 1
                # 아래로 이동
                else:
                    r += 1
            if d < min_d:
                min_d = d
                x = i

    print(f'#{tc} {x}')