from collections import deque


A, B, N, M = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(N)
visited[N] = 0

while q:
    x = q.popleft()
    for y in (x*A, x*B, x+A, x+B, x-A, x-B, x+1, x-1):
        if y == M:
            print(visited[x] + 1)
            exit()
        if 0 <= y < 100000 and visited[y] == -1:
            visited[y] = visited[x] + 1
            q.append(y)