import sys
from itertools import permutations
from copy import deepcopy


input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(K)]
answer = 100 * M

for p in permutations(cmd, K):
    copy_arr = deepcopy(arr)
    for R, C, S in p:
        R -= 1
        C -= 1
        s = 0
        while s < S:
            i = R - S + s
            j = C - S + s
            tmp1 = copy_arr[i][j]
            tmp2 = 0
            while j < C + S - s:
                tmp2 = copy_arr[i][j + 1]
                copy_arr[i][j + 1] = tmp1
                tmp1 = tmp2
                j += 1
            while i < R + S - s:
                tmp2 = copy_arr[i + 1][j]
                copy_arr[i + 1][j] = tmp1
                tmp1 = tmp2
                i += 1
            while j > C - S + s:
                tmp2 = copy_arr[i][j - 1]
                copy_arr[i][j - 1] = tmp1
                tmp1 = tmp2
                j -= 1
            while i > R - S + s:
                tmp2 = copy_arr[i - 1][j]
                copy_arr[i - 1][j] = tmp1
                tmp1 = tmp2
                i -= 1
            s += 1

    for i in range(N):
        answer = min(answer, sum(copy_arr[i]))

print(answer)