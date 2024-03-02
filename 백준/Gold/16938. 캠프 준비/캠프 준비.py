from itertools import combinations

N, L, R, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))
count = 0

for i in range(2, N + 1):
    comb = list(combinations(arr, i))
    for j in comb:
        if L <= sum(j) <= R and j[-1] - j[0] >= X:
            count += 1

print(count)