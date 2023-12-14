import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(set([int(input()) for _ in range(N)]))  # 중복 제거
coins.sort()    # 정렬
# print(coins)

# dp[k]: k원을 거슬러 주는 데 사용한 동전 개수의 최솟값
dp = [K + 1] * (K + 1)

for coin in coins:
    for k in range(K + 1):
        # 아직 초기값이면서, 현재 동전으로 나누어떨어지면
        if dp[k] == K + 1 and k % coin == 0:
            # 현재 동전으로 k원을 만들었을 때의 개수 저장
            dp[k] = k // coin
        # 유지 vs dp[금액 k - 현재 동전의 가치] + 1(i번째 동전 사용)
        if k - coin >= 0:
            dp[k] = min(dp[k], dp[k-coin] + 1)
    # print(dp)

if dp[K] == K + 1:
    print(-1)
else:
    print(dp[K])