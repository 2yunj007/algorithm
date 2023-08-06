import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

cnt = {}

# {10: 0, 9: 0, -5: 0, 2: 0, 3: 0, 4: 0, 5: 0, -10: 0}
for i in check:
    cnt[i] = 0 

for i in nums:
    if i in cnt:
        cnt[i] += 1

for i in check:
    print(cnt[i], end=' ')