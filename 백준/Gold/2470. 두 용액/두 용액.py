import sys
intput = sys.stdin.readline

N = int(input())
sol = sorted(list(map(int, input().split())))

i, j = 0, N - 1
mixed_sol1, mixed_sol2 = 0, 0
sol_char = 10000000000

while i < j:
    sol1, sol2 = sol[i], sol[j]
    tmp = sol1 + sol2

    if tmp == 0:
        mixed_sol1, mixed_sol2 = sol1, sol2
        break

    if abs(tmp) < sol_char:
        sol_char = abs(tmp)
        mixed_sol1, mixed_sol2 = sol1, sol2

    if tmp > 0:
        j -= 1

    if tmp < 0:
        i += 1

print(mixed_sol1, mixed_sol2)