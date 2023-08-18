import sys
input = sys.stdin.readline


def bfs(V, S):
    global cnt
    visited = [0]*(V+1)
    q = [S]
    visited[S] = 1
    while q:
        t = q.pop()
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
                cnt += 1
    return cnt


V = int(input())
E = int(input())
adj_l = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
cnt = 0
print(bfs(V, 1))