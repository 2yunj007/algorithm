from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    visited = [-1] * 101
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        t = q.popleft()
        for m in arr[t]:

            # 100번째 칸에 도착했다면 리턴
            if m == 100:
                return visited[t] + 1

            # 사다리나 뱀이 있는 칸이라면 m 재할당
            if m in sb:
                m = arr[m]

            # 탐색하지 않은 칸이라면 탐색
            if visited[m] == -1:
                q.append(m)
                visited[m] = visited[t] + 1


N, M = map(int, input().split())
arr = [[] for _ in range(101)]
sb = []     # 사다리/뱀 리스트

# 사다리/뱀 정보 입력
for _ in range(N+M):
    s, e = map(int, input().split())
    arr[s] = e
    sb.append(s)

# 주사위로 굴려서 갈 수 있는 칸 정보 입력
for i in range(1, 100):
    # 사다리 혹은 뱀이 아닌 칸에
    if i not in sb:
        for j in range(1, 7):
            # 주사위를 굴린 결과가 100번을 넘어가지 않도록 하여 정보 입력
            if i + j <= 100:
                arr[i].append(i + j)

print(bfs(1))