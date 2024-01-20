N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = P[1]

for i in range(2, N + 1):
    dp[i] = max([P[i]] + [dp[j] + dp[i - j] for j in range(i + 1)])

print(dp[N])