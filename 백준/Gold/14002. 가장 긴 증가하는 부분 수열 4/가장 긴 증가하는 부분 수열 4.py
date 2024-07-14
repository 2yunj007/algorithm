import sys
input = sys.stdin.readline


A = int(input())
arr = list(map(int, input().split()))

dp = [1] * A

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
print(max_len)
ans = []

for i in range(A - 1, -1, -1):
    if dp[i]== max_len:
        ans.append(arr[i])
        max_len -= 1

ans.reverse()
print(*ans)