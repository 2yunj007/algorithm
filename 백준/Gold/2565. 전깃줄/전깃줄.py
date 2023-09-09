import sys
input = sys.stdin.readline
N = int(input())

line = {}   # keys: A, values: B
for i in range(N):
    a, b = map(int, input().split())
    line[a] = b

M = max(line.keys())
dp = [1] * (M+1)

for i in range(1, M+1):
    if i in line.keys():
        for j in range(1, i):
            if j in line.keys():
                if line[i] > line[j]:
                    dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))