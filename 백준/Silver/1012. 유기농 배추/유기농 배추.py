def bfs(N, M):
    visited = [[0]*M for _ in range(N)]
    q = []
    cnt = 0     # 지렁이 수

    # 새로운 배추 묶음 찾을 때마다 수행됨
    while True:
        flag = False  # 다중 for문을 탈출하기 위한 flag
        # 행렬을 탐색하며 방문한 적이 없는 1을 찾음 (단지의 시작 정점)
        for r in range(N):
            for c in range(M):
                if arr[r][c] == 1 and visited[r][c] == 0:
                    q.append([r, c])   # 정점 인큐
                    visited[r][c] = 1  # 방문 표시
                    cnt += 1
                    flag = True
                    break
            if flag:
                break
        else:  # 모든 배추 묶음을 찾았다면 cnt 반환
            return cnt

        while q:  # 큐에 노드가 남아 있을 때까지 반복
            i, j = q.pop(0)  # 제일 먼저 삽입된 노드 디큐
            for k in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 인접 노드 탐색
                ni, nj = i + k[0], j + k[1]
                # 배열에서 벗어나지 않고, 방문하지 않은 노드가 존재할 경우
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append([ni, nj])      # 인큐
                    visited[ni][nj] = 1     # 방문 표시


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    print(bfs(N, M))