import sys
from collections import deque, defaultdict
from itertools import combinations


# 연결이 되어있는지 확인하는 함수
def is_connected(group):
    Q = deque()
    Q.append(group[0])
    visit = [0] * (N+1)
    visit[group[0]] = 1

    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if v in group and visit[v] == 0:
                Q.append(v)
                visit[v] = 1
    for g in group:
        if visit[g] == 0:
            return False
    return True


N = int(sys.stdin.readline().strip())
V_info = [0] + list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
# 인접 행렬을 딕셔너리형태로 받음
for i in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph[i].extend(tmp[1:])

# 정점들
V = [i for i in range(1, N+1)]
rst = 9e9
# 두 그룹으로 나누기 때문에 N//2+1 이상으로 넘어가면 조합이 중복되어 똑같은 작업을 함
for i in range(1, N//2+1):
    # group1에 대해선 itertools사용, group2는 자동적으로 group1을 포함하지 않는 그룹임
    for group1 in combinations(V, i):
        group2 = [j for j in V if j not in group1]
        # 두 그룹에 대해서 연결이 되는 그래프인지 확인
        if is_connected(group1) and is_connected(group2):
            group1_num = sum([V_info[g] for g in group1])
            group2_num = sum([V_info[g] for g in group2])
            rst = min(rst, abs(group1_num-group2_num))
if rst == 9e9:
    print(-1)
else:
    print(rst)