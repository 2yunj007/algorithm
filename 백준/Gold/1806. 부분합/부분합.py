import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

i, j = 0, 0
min_len = 100000
sum_v = nums[0]

while i <= j:
    if sum_v >= S:
        min_len = min(min_len, j - i + 1)
        sum_v -= nums[i]
        i += 1

    else:
        j += 1
        if j == N:
            break
        sum_v += nums[j]

if min_len == 100000: print(0)
else: print(min_len)