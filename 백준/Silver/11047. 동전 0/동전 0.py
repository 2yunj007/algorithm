import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = sorted([int(input()) for _ in range(N)], reverse=True)

rst = 0
for i in range(N):
    cnt, K = divmod(K, coin[i])
    rst += cnt

print(rst)