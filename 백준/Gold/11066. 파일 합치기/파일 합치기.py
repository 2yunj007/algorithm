import sys
input = sys.stdin.readline


def solve():
    K = int(input())
    arr = [0] + list(map(int, input().split()))

    # dp[i][j]는 i번째 파일부터 j번째 파일을 합치는 최소값
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 먼저 dp[i][i+1]을 구함, 두 파일이 연속으로 되어 있을 때의 합을 미리 dp에 저장
    for i in range(1, K + 1):
        for j in range(1, K + 1):
            if j == i + 1:
                dp[i][j] = arr[i] + arr[j]

    # dp의 마지막 행에서부터 위로 올라오면서 dp를 채워 나감
    # dp[1][4]는 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4]와 같은 경우의 수를 가짐
    for i in range(K - 1, 0, -1):
        for j in range(i + 1, K + 1):
            if dp[i][j] == 0:
                dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)]) + sum(arr[i:j + 1])

    print(dp[1][K])


T = int(input())
for _ in range(T):
    solve()