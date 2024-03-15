import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    max_value = 0
    for j in range(i):
        if card[j] < card[i]:
            max_value = max(max_value, dp[j])

    dp[i] = max_value + 1

print(max(dp))