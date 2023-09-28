import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
rst = [[0] * K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            rst[n][k] += A[n][m] * B[m][k]

for i in range(N):
    print(*rst[i])