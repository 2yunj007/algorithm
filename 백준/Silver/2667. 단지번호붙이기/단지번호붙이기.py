def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    cnt = []    # 모든 단지에 속하는 집의 수를 입력받을 리스트
    top = -1

    # 새로운 단지를 찾아야 될 때마다 수행됨
    while True:
        flag = False    # 다중 for문을 탈출하기 위한 flag
        # 행렬을 탐색하며 방문한 적이 없는 1을 찾음 (단지의 시작 정점)
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 1 and visited[r][c] == 0:
                    q.append([r, c])    # 정점 인큐
                    visited[r][c] = 1   # 방문 표시
                    cnt.append(1)       # 카운트 시작
                    top += 1            # bfs를 하면서 카운트를 중첩할 cnt의 인덱스
                    flag = True
                    break
            if flag:
                break
        else:   # 새로운 단지를 찾지 못했다면(모든 단지를 찾았다면) cnt 반환
            return cnt

        while q:    # 큐에 노드가 남아 있을 때까지 반복
            i, j = q.pop(0)    # 제일 먼저 삽입된 노드 디큐
            for k in [[-1, 0], [1, 0], [0, -1], [0, 1]]:    # 인접한 집 탐색
                ni, nj = i+k[0], j+k[1]
                # 지도에서 벗어나지 않고, 방문하지 않은 집이 존재할 경우
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and visited[ni][nj]==0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                    cnt[top] += 1


import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

cnt = sorted(bfs(N))    # 집의 수 오름차순으로 정렬
print(len(cnt))         # 단지 수
for i in cnt:
    print(i)            # 각 단지의 집의 수