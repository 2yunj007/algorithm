import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set([input().rstrip() for _ in range(N)])
see = set([input().rstrip() for _ in range(M)])

rst = sorted(listen.intersection(see))

print(len(rst))
for i in rst:
    print(i)