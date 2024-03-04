import sys
input = sys.stdin.readline

N = int(input())
word = input().rstrip()
BOJ = {'B': 'J', 'O': 'B', 'J': 'O'}

dp = [int(1e9)] * N
dp[0] = 0

for i in range(N):
    for j in range(i):
        if BOJ[word[i]] == word[j]:
            dp[i] = min(dp[i], dp[j] + (j - i)**2)

if dp[N - 1] == int(1e9):
    print(-1)
else:
    print(dp[N - 1])