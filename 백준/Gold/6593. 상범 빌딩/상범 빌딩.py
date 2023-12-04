import sys
input = sys.stdin.readline
from collections import deque
# #: 지나갈 수 없는 칸, .: 비어 있는 칸, S: 시작 지점, E: 탈출 지점

def bfs(sl, sr, sc):
    q = deque()
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    q.append((sl, sr, sc))
    visited[sl][sr][sc] = 0
    direction = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]

    while q:
        l, r, c = q.popleft()
        for d in direction:
            nl, nr, nc = l + d[0], r + d[1], c + d[2]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] != '#' and visited[nl][nr][nc] == -1:
                    q.append((nl, nr, nc))
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    if building[nl][nr][nc] == 'E':
                        return True, visited[nl][nr][nc]
    return False, 0


while True:
    L, R, C = map(int, input().split())  # 층 수, 한 층의 행/열 개수
    if L == R == C == 0:
        break
    building = []
    for i in range(L):
        floor = []
        for j in range(R + 1):
            if j == R:
                input()
            else:
                floor.append(input().strip())
        building.append(floor)

    flag = False
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    is_escaped, x = bfs(l, r, c)
                    flag = True
                    if is_escaped:
                        print(f'Escaped in {x} minute(s).')
                    else:
                        print('Trapped!')
                    break
            if flag:
                break
        if flag:
            break