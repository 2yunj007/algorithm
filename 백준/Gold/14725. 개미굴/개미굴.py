import sys
input = sys.stdin.readline

foods = []
N = int(input())
for _ in range(N):
    K, *food = input().split()
    foods.append(food)

foods.sort()

dash = '--'
answer = []
for i in range(N):
    # 첫 번째는 중복이 없으므로 그대로 출력
    if i == 0:
        for j in range(len(foods[i])):
            answer.append(dash * j + foods[i][j])
    else:
        idx = 0
        for j in range(len(foods[i])):
            # 이전 리스트가 현재 리스트와 겹치지 않을 때
            if foods[i - 1][j] != foods[i][j] or len(foods[i - 1]) <= j:
                break
            # 겹치는 원소가 존재한다면 해당 원소를 출력할 필요가 없으므로 건너뜀
            else:
                idx = j + 1
        for j in range(idx, len(foods[i])):
            answer.append(dash * j + foods[i][j])

for ans in answer:
    print(ans)