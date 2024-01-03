import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
distance = [[0] * N for _ in range(N)]

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if not distance[i][j]:
                d = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2
                distance[i][j], distance[j][i] = d, d
            if not distance[i][k]:
                d = (arr[i][0] - arr[k][0])**2 + (arr[i][1] - arr[k][1])**2
                distance[i][k], distance[k][i] = d, d
            if not distance[j][k]:
                d = (arr[j][0] - arr[k][0])**2 + (arr[j][1] - arr[k][1])**2
                distance[j][k], distance[k][j] = d, d

            d1, d2, d3 = distance[i][j], distance[i][k], distance[j][k]
            if 2*max(d1, d2, d3) == d1 + d2 + d3:
                answer += 1

print(answer)