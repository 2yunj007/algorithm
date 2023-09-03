import sys


def f(N):
    dp = [0]*N
    dp[0] = nums[0]
    for i in range(1, N):
        if dp[i-1] + nums[i] > nums[i]:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
print(f(N))