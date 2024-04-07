R, C, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dp = [[0] * (C + 1) for _ in range(R + 1)]

for r in range(R):
    for c in range(C):
        dp[r + 1][c + 1] = dp[r][c + 1] + dp[r + 1][c] - dp[r][c] + arr[r][c]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    num = (r2 - r1 + 1) * (c2 - c1 + 1)

    print((dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 -1][c1 - 1]) // num)