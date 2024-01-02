N = int(input())
dp = [0] * N
dp[0] = float(input())
for i in range(1, N):
    num = float(input())
    dp[i] = max(dp[i - 1] * num, num)
print('%0.3f' % max(dp))