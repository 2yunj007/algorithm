# 카탈란의 수
# i = 0부터 i = N까지의 모든 i에 대해,
# Cn+1 = Sigma(Ci * Cn-i)
# 여는 괄호와 닫는 괄호로 만들 수 있는 올바른 괄호 구조의 가짓수를 구하는 문제에서 사용
# 해당 문제도 비슷한 유형
# 하나의 약(열린 괄호)을 꺼내는 총 횟수 = N
# 반 개의 약(닫힌 괄호)을 꺼내는 횟수는 하나의 약을 꺼내는 횟수를 초과할 수 없음

MAX = 30

dp = [0] * (MAX + 1)
dp[0] = 1

for i in range(1, MAX + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - 1 - j]

while True:
    N = int(input())

    if N == 0:
        break

    print(dp[N])