def attack(row, col, dir):
    global ans_score
    ans_score += 1
    ans[row][col] = 'F'
    dr, dc = D[dir]
    for i in range(1, arr[row][col]):
        nr, nc = row + dr*i, col + dc*i
        if 0 <= nr < N and 0 <= nc < M and ans[nr][nc] == 'S':
            attack(nr, nc, dir)


def defense(row, col):
    ans[row][col] = 'S'


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

ans_score = 0
ans = [['S'] * M for _ in range(N)]

for _ in range(R*2):
    cmd = tuple(input().split())
    if len(cmd) == 3:
        attack(int(cmd[0])-1, int(cmd[1])-1, cmd[2])
    else:
        defense(int(cmd[0])-1, int(cmd[1])-1)

print(ans_score)
for i in range(N):
    print(*ans[i])