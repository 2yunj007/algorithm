M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

answer = 0

save = [[0 for _ in range(N)] for _ in range(M)]    # 범위 내 로봇들의 출력 값 중 최댓값
output = [[0 for _ in range(N)] for _ in range(M)]  # 저장 값 + 가중치

# 가장 왼쪽에 있는 열의 입력 값은 0이므로 저장 값은 0, 출력 값은 가중치가 됨
for i in range(M):
    output[i][0] = arr[i][0]

for j in range(1, N):
    for i in range(M):
        # (i, j)의 저장 값은 범위 내의 로봇 중 j-1 열에 있는 저장 값들의 최댓갑
        if i == 0:
            save[i][j] = max(output[i][j - 1], output[i + 1][j - 1])
        elif i == M - 1:
            save[i][j] = max(output[i - 1][j - 1], output[i][j - 1])
        else:
            save[i][j] = max(output[i + 1][j - 1], output[i][j - 1], output[i - 1][j - 1])

        output[i][j] = save[i][j] + arr[i][j]
        answer = max(answer, save[i][j])

print(answer)