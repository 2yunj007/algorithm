import sys
input = sys.stdin.readline
import heapq


N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]

lecture.sort(key=lambda x: x[1])

room = []
heapq.heappush(room, lecture[0][2])

for i in range(1, N):
    if lecture[i][1] < room[0]:
        heapq.heappush(room, lecture[i][2])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][2])

print(len(room))