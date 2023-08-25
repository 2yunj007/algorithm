N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

xy.sort()
xy.sort(key=lambda x:x[1])

for i in xy:
    print(*i)