'''
arr = 1 2 1 3
 dp = 1 1 1 1
 dp = 1 2 1 1, i=1
 dp = 1 2 1 1, i=2
 dp = 1 2 1 2, i=3, j=0
 dp = 1 2 1 3, i=3, j=1
'''

import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))