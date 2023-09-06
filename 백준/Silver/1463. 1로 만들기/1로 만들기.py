from collections import deque

N = int(input())
dp = [0] * (N+1)
q = deque([N])

while q:    # bfs
    t = q.popleft()
    if t == 1:
        break
    if t % 3 == 0 and dp[t//3] == 0:
        q.append(t//3)
        dp[t//3] = dp[t] + 1
    if t % 2 == 0 and dp[t//2] == 0:
        q.append(t//2)
        dp[t//2] = dp[t] + 1
    if dp[t-1] == 0:
        q.append(t-1)
        dp[t-1] = dp[t] + 1
        
print(dp[1])