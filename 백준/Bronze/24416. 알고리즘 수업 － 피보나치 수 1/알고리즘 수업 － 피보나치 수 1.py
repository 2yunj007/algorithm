def fibo(n):
    dp = [0]*(n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 재귀 호출 카운터는 피보나치 수만큼 진행
# dp는 3부터 n까지 for문을 돌리기 때문에 n-2만큼 진행
n = int(input())
print(fibo(n), n-2)