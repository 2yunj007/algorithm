N = int(input())
balls = input()
answer = 1e9

for i in range(2):
    if i == 0: color = 'R'
    else: color = 'B'

    for j in range(2):
        if j == 0: K = range(N - 1, -1, -1)
        else:   K = range(N)

        for k in K:
            if balls[k] != color:
                if j == 0:
                    answer = min(answer, balls[:k].count(color))
                else:
                    answer = min(answer, balls[k:].count(color))
                break

print(answer)