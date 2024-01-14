from itertools import permutations


def get_score(seq):
    score = 0
    i = 0

    for ining in range(N):
        base = [0, 0, 0, 0]
        out = 0
        while out < 3:
            if not baseball(seq[i], base, ining):
                out += 1

            i = (i + 1) % 9

        score += base[3]

    return score


def baseball(i, base, ining):
    shoot = player[ining][i]

    if shoot == 1:      # 안타
        base[3] += base[2]
        base[2] = base[1]
        base[1] = base[0]
        base[0] = 1

    elif shoot == 2:    # 2루타
        base[3] += base[2] + base[1]
        base[2] = base[0]
        base[1] = 1
        base[0] = 0

    elif shoot == 3:    # 3루타
        base[3] += base[2] + base[1] + base[0]
        base[2] = 1
        base[1] = base[0] = 0

    elif shoot == 4:    # 홈런
        base[3] += base[2] + base[1] + base[0] + 1
        base[2] = base[1] = base[0] = 0

    else:   # 아웃
        return False

    return True


N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]

permutations_result = list(permutations(range(1, 9)))

answer = 0
for perm in permutations_result:
    perm = list(perm)
    perm.insert(3, 0)
    answer = max(answer, get_score(perm))

print(answer)