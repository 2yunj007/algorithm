from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [1e9] * N
q = deque()
q.append(0)
dp[0] = 0

for i in range(N):
    for j in range(1, A[i] + 1):
        if i + j >= N:
            continue
        if dp[i] + 1 > dp[i + j]:
            continue
        dp[i + j] = dp[i] + 1
        q.append(i + j)

if dp[N - 1] == 1e9:
    print(-1)
else:
    print(dp[N - 1])