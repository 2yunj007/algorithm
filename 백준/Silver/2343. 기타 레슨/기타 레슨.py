import sys
input = sys.stdin.readline


N, M = map(int, input().split())
blue = list(map(int, input().split()))
answer = 0

start = max(blue)
end = sum(blue)

while start <= end:
    mid = (start + end) // 2

    _sum = 0
    count = 1

    for i in range(N):
        if _sum + blue[i] > mid:
            count += 1
            _sum = 0

        _sum += blue[i]

    if count <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)