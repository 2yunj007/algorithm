N, M = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])

party = []
for i in range(M):
    party.append(set(list(map(int, input().split()))[1:]))

for i in range(M):
    for j in range(M):
        # 진실을 아는 사람이 포함되어 있으면 진실 집합에 포함시킴
        if party[j] & truth:
            truth |= party[j]

answer = 0
for i in range(M):
    if not(party[i] & truth):
        answer += 1

print(answer)