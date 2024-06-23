import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jews = [int(input()) for _ in range(M)]

end = max(jews)
start = 1
answer = 0

while start <= end:
    mid = (start + end) // 2

    # mid 개로 보석을 나누어 줬을 때 받을 수 있는 학생의 수
    receiver = 0

    for jew in jews:
        receiver += jew // mid

        # 남은 보석을 가져가는 학생
        if jew % mid:
            receiver += 1

    # 학생 수를 초과하면 나누어 주는 보석 개수 증가
    if receiver > N:
        start = mid + 1

    # 학생 수 이하이면 나누어 주는 보석 개수 감소
    elif receiver <= N:
        end = mid - 1
        answer = mid

print(answer)