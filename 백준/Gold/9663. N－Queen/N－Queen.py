def check(r):
    for i in range(r):
        # 같은 열에 놓여질 경우
        if row[r] == row[i]:
            return False
        # 대각선 경로와 겹치는 경우
        # = 행의 차가 열의 차와 같은 경우
        if abs(r - i) == abs(row[r] - row[i]):
            return False
    return True


def n_queen(r):
    global cnt
    # N-1번째 행까지 퀸을 다 놓았다면
    if r == N:
        cnt += 1
        return

    for c in range(N):
        # [r, c]에 놓음
        row[r] = c
        # 이전에 놓은 퀸들의 경로와 겹치는지 확인
        if check(r):
            n_queen(r + 1)


N = int(input())
row = [0] * N
cnt = 0
n_queen(0)
print(cnt)