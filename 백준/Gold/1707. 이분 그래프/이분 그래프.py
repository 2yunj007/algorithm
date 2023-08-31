from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        t = q.popleft()
        for w in arr[t]:
            if not visited[w]:                  # 아직 방문하지 않았다면
                q.append(w)                     # 인큐 하고
                visited[w] = -visited[t]        # 정점과 다른 수로 방문 표시
            elif visited[w] == visited[t]:      # 방문했는데 정점과 같은 수로 방문 표시되어 있다면
                return False                    # 이분 그래프 x
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V + 1)

    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    flag = True
    for i in range(1, V+1):
        if not visited[i]:
            if not bfs(i):
                flag = False
                break

    if flag: print('YES')
    else: print('NO')