import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

cnt = {}
for i in range(N):
    cnt.setdefault(arr[i], 0)
    cnt[arr[i]] += 1

mode_lst = []
max_cnt = max(cnt.values())
for i in cnt.keys():
    if cnt[i] == max_cnt and len(mode_lst) < 2:
        mode_lst.append(i)

average = round(sum(arr) / N)   # 산술평균
center = arr[N // 2]            # 중앙값
mode = mode_lst[-1]             # 최빈값
rng = arr[N - 1] - arr[0]       # 범위

print(average)
print(center)
print(mode)
print(rng)