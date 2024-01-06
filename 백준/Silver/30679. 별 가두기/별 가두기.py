def star(r, c):
    dir = [[-1] * M for _ in range(N)]
    dir[r][c] = 0
    d = 0
    while True:
        n = arr[r][c]
        r, c = r + D[d][0]*n, c + D[d][1]*n
        d = (d + 1) % 4

        if 0 <= r < N and 0 <= c < M:
            # 같은 곳에 같은 방향으로 방문한 적이 있다면 가두기 성공
            if dir[r][c] == d:
                return True
            # 없다면 방향 저장
            else:
                dir[r][c] = d
        # 범위 벗어나면 실패
        else:
            return False


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = ((0, 1), (1, 0), (0, -1), (-1, 0))

answer = [0, []]
for r in range(N):
    if star(r, 0):
        answer[0] += 1
        answer[1].append(r + 1)

print(answer[0])
print(*answer[1])