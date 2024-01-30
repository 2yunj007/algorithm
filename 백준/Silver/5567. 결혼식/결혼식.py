from collections import deque

n = int(input())
m = int(input())
arr = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = True
    arr[b-1][a-1] = True

q = deque()
q.append(0)
visited = [0] * n

while q:
    t = q.popleft()
    for i in range(n):
        if arr[t][i] and not visited[i]:
            visited[i] = visited[t] + 1
            q.append(i)

answer = 0
for i in range(1, n):
    if 0 < visited[i] < 3:
        answer += 1

print(answer)