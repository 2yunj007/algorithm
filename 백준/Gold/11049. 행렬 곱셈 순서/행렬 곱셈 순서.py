import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(2, N+1):    # 부분 행렬의 길이
    for j in range(N-i+1):   # 시작점
        dp[j][j+i-1] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬

        for k in range(i-1):
            dp[j][j+i-1] = min(
                dp[j][j+i-1],
                dp[j][j+k] + dp[j+k+1][j+i-1] + arr[j][0] * arr[j+k][1] * arr[j+i-1][1]
            )

print(dp[0][N - 1])