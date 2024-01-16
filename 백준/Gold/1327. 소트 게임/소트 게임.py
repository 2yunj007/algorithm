from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = set()
    visited.add(''.join(nums))
    q = deque([(nums, 0)])

    while q:
        now, cnt = q.popleft()

        if now == nums_sorted:
            return cnt

        for i in range(N - K + 1):
            next = now[:i] + now[i:i+K][::-1] + now[i+K:]

            next_str = ''.join(next)
            if next_str not in visited:
                q.append((next, cnt + 1))
                visited.add(next_str)

    return -1


N, K = map(int, input().split())
nums = list(input().split())
nums_sorted = sorted(nums)
print(bfs())