def rgb(N):
    dp = [[0]*3 for _ in range(N)]
    dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]
    for i in range(1, N):

        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])    # i번째 고른 것이 R
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])    # G
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])    # B
    return min(dp[N-1][0], dp[N-1][1], dp[N-1][2])


import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(rgb(N))