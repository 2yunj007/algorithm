# 걸리는 시간이 적은 사람부터 사용

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()

for i in range(1, N):
    P[i] += P[i-1]

print(sum(P))