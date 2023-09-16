import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        cnt.setdefault(word, 0)
        cnt[word] += 1

lst = []
for s in cnt.keys():
    lst.append([-cnt[s], -len(s), s])

lst.sort()

for i in range(len(lst)):
    print(lst[i][2])