import sys
input = sys.stdin.readline

S = input()
N = len(S)
q = int(input())
# 알파벳 개수를 열로 하고 문자열 길이를 행으로 하는 배열
arr = [[0]*26 for _ in range(N)]

# i번째 문자 카운트
for i in range(N-1):
    n = ord(S[i]) - 97
    arr[i][n] = 1

    # 모든 알파벳에 대하여 이전 행의 카운트를 누적
    for j in range(26):
        arr[i][j] += arr[i-1][j]

for _ in range(q):
    a, *s = input().split()
    l, r = map(int, s)
    n = ord(a) - 97

    if l == 0:
        print(arr[r][n])
    else:
        print(arr[r][n] - arr[l-1][n])
