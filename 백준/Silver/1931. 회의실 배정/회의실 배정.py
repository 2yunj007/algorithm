import sys
input = sys.stdin.readline

N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]

# 종료 시간을 기준으로 정렬
meet.sort(key=lambda x:[x[1], x[0]])

cnt = 1
last = meet[0][1]
for i in range(1, N):
    # 마지막으로 저장된 회의의 종료 시간보다 늦거나 같으면 다음 회의로 선정
    if meet[i][0] >= last:
        cnt += 1
        last = meet[i][1]

print(cnt)