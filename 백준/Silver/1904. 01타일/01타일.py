'''
N=1, 1
N=2, 2
N=3, 3
N=4, 5
N=5, 8
# 반복문 내에서 나머지 연산을 하지 않으면 값이 int 값을 초과해 메모리 초과 발생
'''


def f(N):
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[N]


N = int(input())
print(f(N))