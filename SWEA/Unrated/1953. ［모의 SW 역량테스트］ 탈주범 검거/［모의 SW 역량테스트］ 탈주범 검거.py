def bfs(R, C):
    global L
    visited = [[0] * M for _ in range(N)]
    q = [[R, C]]    # 맨홀의 위치를 인큐 해 둠
    visited[R][C] = 1
    cnt = 0     # 탈주범이 있을 수 있는 영역의 수

    while q:    # 큐에 값이 있을 동안 반복
        i, j = q.pop(0)

        # L의 시간이 흘렀으면 방문한 통로의 수를 셈
        if visited[i][j] == L:
            for r in range(N):
                for c in range(M):
                    if visited[r][c] != 0:
                        cnt += 1
            return cnt

        for k in tp[arr[i][j]]:   # 해당 위치의 map 값 == type
            ni = i + d[k][0]
            nj = j + d[k][1]

            # 지도를 벗어나지 않고 방문하지 않았으며 arr에 값이 존재하는 경우
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj]:

                # 통로가 연결되어 있는지 확인
                # 현재 위로 가는데 이동할 통로의 아래와 연결되어 있다면
                if k == 0 and 1 in tp[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

                # 현재 아래로 가는데 이동할 통로의 위와 연결되어 있다면
                elif k == 1 and 0 in tp[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

                # 현재 왼쪽으로 가는데 이동할 통로의 오른쪽과 연결되어 있다면
                elif k == 2 and 3 in tp[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

                # 현재 오른쪽으로 가는데 이동할 통로의 왼쪽과 연결되어 있다면
                elif k == 3 and 2 in tp[arr[ni][nj]]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

                # 통로가 연결되어 있지 않으면
                else:
                    pass

    # L 미만의 시간 동안 모든 통로에 방문하여 while문이 종료된다면 현재까지 방문한 영역의 수 반환
    for r in range(N):
        for c in range(M):
            if visited[r][c] != 0:
                cnt += 1
    return cnt
    

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # 지도 크기, 맨홀 뚜껑 위치, 소요 시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
    # 인덱스가 터널 구조물 타입, 내부 리스트가 기능을 나타내는 d의 인덱스
    tp = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

    print(f'#{tc} {bfs(R, C)}')