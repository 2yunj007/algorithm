N = int(input())
MOD = 1000000000

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    if i % 2:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % MOD

print(dp[N])