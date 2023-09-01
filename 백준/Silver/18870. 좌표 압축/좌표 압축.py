import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
X_set = sorted(set(X))
rst = {}

for i in range(len(X_set)):
    rst[X_set[i]] = i

for i in range(N):
    print(rst[X[i]], end=' ')