import sys
input = sys.stdin.readline

N, M, r, c, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]   # 초기 상태: 6, 5, 3, 2, 4, 1
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


def rolling_dice(command):
    new_dice = [0, 0, 0, 0, 0, 0]
    if command == 1:
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
    if command == 2:
        new_dice[0] = dice[4]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[2]
    if command == 3:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
    if command == 4:
        new_dice[0] = dice[3]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
    return new_dice


for k in range(K):
    command = commands[k]
    nr, nc = r + d[command][0], c + d[command][1]
    if 0 <= nr < N and 0 <= nc < M:
        r, c = nr, nc
        dice = rolling_dice(command)
        if arr[r][c] == 0:
            arr[r][c] = dice[0]
        else:
            dice[0] = arr[r][c]
            arr[r][c] = 0
        print(dice[5])