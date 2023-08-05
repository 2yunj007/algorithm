import sys
N = int(sys.stdin.readline())
cards = sorted((map(int, sys.stdin.readline().split())))
M = int(input())
find_cards = list(map(int, input().split()))

rst = [0] * M

# 이진 탐색
for i in range(M):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if cards[middle] == find_cards[i]:
            rst[i] = 1
            break
        elif cards[middle] > find_cards[i]:
            end = middle - 1
        else:
            start = middle + 1

print(*rst)