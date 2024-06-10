import heapq

N = int(input())

hq = []
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))

task = [0] * 1001
answer = 0

while hq:
    w, d = heapq.heappop(hq)
    w = -w

    for i in range(d, 0, -1):
        if task[i]:
            continue

        task[i] = 1
        answer += w
        break

print(answer)