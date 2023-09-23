def make_team(i):
    global t
    if i == N // 2:
        # 점수 구하기
        ability.append(0)
        for q in range(N // 2):
            for p in range(q + 1, N // 2):
                r, c = team[q], team[p]
                ability[t] += arr[r][c] + arr[c][r]
        t += 1
        return

    for j in range(N):
        # 이미 포함되어 있다면
        if j in team:
            continue
        # 팀을 오름차순으로만 구성 (중복 제거)
        if i > 0 and team[i - 1] > j:
            continue
        team[i] = j
        make_team(i + 1)
        team[i] = -1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
team = [-1] * (N // 2)
ability = []
t = 0
make_team(0)

rst = int(1e9)
M = len(ability)

# 두 팀의 점수 차 계산
for i in range(M // 2):
    rst = min(rst, abs(ability[i] - ability[M - i - 1]))
print(rst)