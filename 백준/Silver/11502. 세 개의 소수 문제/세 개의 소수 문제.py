from itertools import product

maxK = 1000
p = [False, False] + [True for _ in range(maxK-1)]

for i in range(2, int(maxK**0.5)+1):
    for j in range(i*2, maxK+1, i):
        p[j] = False

plist = []

for i in range(1001):
    if p[i]:
        plist.append(i)

combs = list(product(plist, repeat=3))

for _ in range(int(input())):
    K = int(input())

    for comb in combs:
        sum_ = sum(comb)
        if sum_ == K:
            print(*comb)
            break