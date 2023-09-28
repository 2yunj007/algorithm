N = int(input())
arr = [0] + sorted([int(input()) for _ in range(N)])
rst = 0
for i in range(1, N + 1):
    rst += abs(i - arr[i])
print(rst)