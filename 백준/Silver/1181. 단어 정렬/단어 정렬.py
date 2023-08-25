N = int(input())
s = list(set([input() for _ in range(N)]))
lst = []

for i in s:
    lst.append([len(i), i])

lst.sort()

for a, b in lst:
    print(b)