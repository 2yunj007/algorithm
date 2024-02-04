def f1():
    answer = []
    k = arr[1]
    for i in range(N, 0, -1):
        rng = fac[i - 1]
        p = (k - 1) // rng
        answer.append(pri[p] + 1)
        k -= rng * p
        pri.pop(p)
    print(*answer)


def f2():
    answer = 1
    for i in range(1, N + 1):
        rng = fac[N - i]
        p = pri.index(arr[i])
        answer += rng * (p - 1)
        pri.pop(p)
    print(answer)


N = int(input())
arr = list(map(int, input().split()))

# factorial
fac = [1] * N
for i in range(2, N):
    fac[i] = fac[i - 1] * i

# priority
pri = list(range(N + 1))

if arr[0] == 1:
    f1()
else:
    f2()