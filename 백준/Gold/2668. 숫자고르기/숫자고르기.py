def dfs(node, start):
    visited[node] = True
    next_node = nums[node]

    if next_node == start or visited[next_node]:
        answer.add(next_node)
        return True

    dfs(next_node, start)


N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
answer = set()

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

answer = sorted(list(answer))

print(len(answer))

for i in answer:
    print(i)