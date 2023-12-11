from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [[deque() for _ in range(N)] for _ in range(N)]    # 3차원 행렬
D = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
balls = {}

num_ball = M
for i in range(1, M + 1):
    r, c, m, s, d = map(int, input().split())
    balls.setdefault(i, {'r': r-1, 'c': c-1, 'm': m, 's': s, 'd': d})
    arr[r-1][c-1].append(i)


def move(num):
    global total_m
    r, c, d, s = balls[num]['r'], balls[num]['c'], balls[num]['d'], balls[num]['s']
    nr, nc = (r + D[d][0] * s) % N, (c + D[d][1] * s) % N

    # 이동
    balls[num]['r'], balls[num]['c'] = nr, nc
    arr[nr][nc].append(num)
    moved.append(num)


def separation(r, c):
    global num_ball, total_m
    sum_m, sum_s, sum_d = 0, 0, set()
    for i in arr[r][c]:
        sum_m += balls[i]['m']
        sum_s += balls[i]['s']
        if balls[i]['d'] % 2 == 0:  # 짝수면 1, 홀수면 1을 세트에 저장
            sum_d.add(1)
        else:
            sum_d.add(0)

    # 질량 결정
    new_m = sum_m // 5
    # 질량이 0이면 소멸
    if new_m == 0:
        arr[r][c] = deque()
        return

    # 방향 결정
    new_d = []
    if len(sum_d) == 1:  # 모두 홀수 또는 짝수인 경우 길이는 1
        new_d = [0, 2, 4, 6]
    else:
        new_d = [1, 3, 5, 7]

    # 속력 결정
    new_s = sum_s // len(arr[r][c])

    # 새로운 파이어볼 4개 생성
    new_balls = deque()
    for i in range(4):
        num_ball += 1
        new_balls.append(num_ball)
        balls.setdefault(num_ball, {'r': r, 'c': c, 'm': new_m, 's': new_s, 'd': new_d[i]})
    arr[r][c] = new_balls


for k in range(K):
    moved = []
    for r in range(N):
        for c in range(N):
            while arr[r][c]:
                # 이미 이동한 파이어볼이 나오면 이동 중지
                if arr[r][c][0] in moved:
                    break
                i = arr[r][c].popleft()
                move(i)     # 이동

    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) >= 2:
                separation(r, c)    # 분리

total_m = 0
for r in range(N):
    for c in range(N):
        for i in arr[r][c]:
            total_m += balls[i]['m']
print(total_m)