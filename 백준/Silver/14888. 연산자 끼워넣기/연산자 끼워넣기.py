import sys
input = sys.stdin.readline


def dfs(i, total, plus, sub, mul, div):
    global max_v, min_v
    if i == N:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        return

    if plus:
        dfs(i + 1, total + num[i], plus - 1, sub, mul, div)
    if sub:
        dfs(i + 1, total - num[i], plus, sub - 1, mul, div)
    if mul:
        dfs(i + 1, total * num[i], plus, sub, mul - 1, div)
    if div:
        dfs(i + 1, int(total / num[i]), plus, sub, mul, div - 1)
        # if total < 0:
        #     total = -(-total // num[i])
        # else:
        #     total = total // num[i]
        # dfs(i + 1, total, plus, sub, mul, div - 1)


N = int(input())
num = list(map(int, input().split()))
opr = list(map(int, input().split()))
max_v = -1e10
min_v = 1e10
dfs(1, num[0], opr[0], opr[1], opr[2], opr[3])
print(max_v)
print(min_v)