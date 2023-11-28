import heapq


def dijkstra(start, end):
    distance = [1e9] * (100001)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for cost, next in ((1, now - 1), (1, now + 1), (0, now * 2)):
            if 0 <= next <= 100000:
                new_dist = dist + cost

                if distance[next] <= new_dist:
                    continue

                distance[next] = new_dist
                heapq.heappush(pq, (new_dist, next))

    return distance[end]


N, K = map(int, input().split())

result = dijkstra(N, K)

print(result)