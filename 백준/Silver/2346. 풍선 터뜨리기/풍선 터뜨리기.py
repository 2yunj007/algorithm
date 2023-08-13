from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
deq = deque(enumerate(map(int, input().split()), start=1))
# deque([(1, 3), (2, 2), (3, 1), (4, -3), (5, -1)])

for i in range(N):
    # 첫 번째 풍선 터뜨리고 그 수만큼 덱을 회전시킴
    idx, n = deq.popleft()
    if n > 0:
        # 오른쪽에 있는 걸 삭제해야 하기 떄문에 왼쪽으로 회전
        # 이미 한 칸 밀려 있으니까 -1
        deq.rotate(-(n-1))
    else:
        # 왼쪽에 있는 걸 삭제해야 하기 떄문에 오른쪽으로 회전
        deq.rotate(-n)
    print(idx, end=' ')