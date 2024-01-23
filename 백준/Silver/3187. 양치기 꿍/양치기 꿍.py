from collections import deque

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
visited = [[0] * C for _ in range(R)]
answer = [0, 0]

for r in range(R):
    for c in range(C):
        if arr[r][c] != '#' and not visited[r][c]:
            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            v_cnt, k_cnt = 0, 0

            while q:
                i, j = q.popleft()

                if arr[i][j] == 'v':
                    v_cnt += 1
                elif arr[i][j] == 'k':
                    k_cnt += 1

                for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != '#' and not visited[ni][nj]:
                        q.append((ni, nj))
                        visited[ni][nj] = 1

            if v_cnt >= k_cnt:
                answer[1] += v_cnt
            else:
                answer[0] += k_cnt

print(*answer)