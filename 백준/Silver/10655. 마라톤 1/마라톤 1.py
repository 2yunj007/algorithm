import sys
input = sys.stdin.readline

def cal_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

N = int(input())

point = {}
for i in range(N):
    point.setdefault(i, {'x': 0, 'y': 0})
    x, y = map(int, input().split())
    point[i]['x'], point[i]['y'] = x, y

distance1 = [0] * N
# 이전 번호와의 거리
for i in range(1, N):
    distance1[i] = cal_distance(point[i-1]['x'], point[i-1]['y'], point[i]['x'], point[i]['y'])
# print(distance1)

distance2 = [0] * N
# i 번을 건너뛰었을 때의 거리
for i in range(1, N-1):
    distance2[i] = cal_distance(point[i-1]['x'], point[i-1]['y'], point[i+1]['x'], point[i+1]['y'])
# print(distance2)

total_distance = sum(distance1)
min_distance = float('inf')
for i in range(1, N-1):
    min_distance = min(min_distance, total_distance - distance1[i] - distance1[i+1] + distance2[i])

print(min_distance)