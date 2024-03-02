import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]
answer = 0

start, end = min(times) * (M // N), max(times) * M

while start <= end:
    mid = (start + end) // 2
    people = 0

    for time in times:
        people += mid // time

    if people >= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)