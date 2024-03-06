from collections import deque
import sys
input = sys.stdin.readline


def pang(row, col, color):
    q = deque([(row, col)])
    visited = [(row, col)]

    while q:
        i, j = q.popleft()
        for d in D:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < 12 and 0 <= nj < 6:
                if arr[ni][nj] == color and (ni, nj) not in visited:
                    q.append((ni, nj))
                    visited.append((ni, nj))

    if len(visited) >= 4:
        for i, j in visited:
            arr[i][j] = '.'
        return True
    else:
        return False


def down():
    new_arr = [[] for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if arr[j][i] != '.':
                new_arr[i].append(arr[j][i])

    for j in range(6):
        for i in range(12 - len(new_arr[j])):
            arr[i][j] = '.'
        for i in range(len(new_arr[j])):
            arr[11 - len(new_arr[j]) + i + 1][j] = new_arr[j][i]


answer = 0
arr = [list(input().rstrip()) for _ in range(12)]
D = ((-1, 0), (1, 0), (0, -1), (0, 1))

while True:
    flag = False
    for r in range(11, -1, -1):
        for c in range(6):
            if arr[r][c] != '.':
                if pang(r, c, arr[r][c]):
                    flag = True
    if not flag:
        break
    else:
        answer += 1
        down()

print(answer)