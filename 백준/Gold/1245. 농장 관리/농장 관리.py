def dfs(i, j, visited):
    global is_top
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        ni, nj = i + dx, j + dy

        # 범위를 벗어나거나 이미 방문했을 경우
        if not(0 <= ni < N and 0 <= nj < M) or (ni, nj) in visited:
            continue

        # 인접한 격자가 더 높은 경우 => 봉우리가 아님
        if arr[ni][nj] > arr[i][j]:
            is_top = False
            return
        # 인접한 격자와 높이가 같은 경우 => 봉우리 집합일 가능성 있음
        elif arr[ni][nj] == arr[i][j]:
            visited.append((ni, nj))
            checked[ni][nj] = True
            dfs(ni, nj, visited)
        # 인접한 격자가 더 낮은 경우 => 해당 인접한 격자는 봉우리가 될 수 없음
        else:
            visited.append((ni, nj))
            checked[ni][nj] = True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

checked = [[False] * M for _ in range(N)]   # 봉우리인지 아닌지 체크 완료된 좌표

for r in range(N):
    for c in range(M):
        if arr[r][c] and not checked[r][c]:
            checked[r][c] = True
            is_top = True
            dfs(r, c, [(r, c)])

            if is_top:
                answer += 1

print(answer)