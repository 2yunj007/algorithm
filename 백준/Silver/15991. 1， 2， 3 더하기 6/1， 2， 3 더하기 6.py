dp = [0] * 100001

j = [1, 1, 2, 2, 3, 3]
for i in range(6):
    dp[i] = j[i]

for i in range(6, 100001):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009

for _ in range(int(input())):
    N = int(input())
    print(dp[N])