import sys
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
cctv = []
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] in [1, 2, 3, 4, 5]:
            cctv.append([row[j], i, j])

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
def upd(board, current_mode, y, x):
    for i in current_mode:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                break
            if board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                board[ny][nx] = 7

def dfs(depth, matrix):
    global min_value

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += matrix[i].count(0)
        min_value = min(min_value, count)
        return
    tmp = copy.deepcopy(matrix)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        upd(tmp, i, x, y)
        dfs(depth+1, tmp)
        tmp = copy.deepcopy(matrix)

min_value = int(1e9)
dfs(0, matrix)
print(min_value)