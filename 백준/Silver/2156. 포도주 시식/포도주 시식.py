N = int(input())
a = [0]*(N+2)
dp = [0]*(N+2)
for i in range(N):
    a[i] = int(input())

dp[0] = a[0]
dp[1] =a[0] + a[1]
dp[2] = max(dp[1], a[2]+a[1], a[2]+a[0])

# 1. 현재 값을 더하지 않음
# 2. 현재 값 + 첫 번째 전 값 + 세 번째 전까지의 dp 값
# 3. 현재 값 + 두 번째 전까지의 dp 값
for i in range(3, N):
    dp[i] = max(dp[i-1], a[i]+a[i-1]+dp[i-3], a[i]+dp[i-2])
print(max(dp))