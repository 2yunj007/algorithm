for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M + 1):
            # coin으로 i를 만드는 경우의 수는 i - coin을 만드는 경우의 수
            dp[i] += dp[i - coin]

    print(dp[M])