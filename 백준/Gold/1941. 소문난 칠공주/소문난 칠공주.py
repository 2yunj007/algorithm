import sys
from itertools import combinations
from collections import deque


input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(5)]
answer = 0

coors = []

for i in range(5):
    for j in range(5):
        coors.append((i, j))

combs = list(combinations(coors, 7))

for comb in combs:
    tmp_arr = [[0] * 5 for _ in range(5)]
    Y = 0
    is_possible = True

    for r, c in comb:
        if arr[r][c] == "Y":
            Y += 1

        if Y > 3:
            is_possible = False
            break

        tmp_arr[r][c] = 1

    if not is_possible:
        continue

    visited = [[0] * 5 for _ in range(5)]
    q = deque()

    q.append((comb[0][0], comb[0][1]))
    visited[comb[0][0]][comb[0][1]] = 1
    count = 1

    while q:
        r, c = q.popleft()

        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + d[0], c + d[1]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and tmp_arr[nr][nc]:
                count += 1
                visited[nr][nc] = 1
                q.append((nr, nc))

    if count == 7:
        answer += 1

print(answer)