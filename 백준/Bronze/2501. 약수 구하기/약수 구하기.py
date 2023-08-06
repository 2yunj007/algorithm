import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []
cnt = 0

for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break

if cnt < K:
    print(0)