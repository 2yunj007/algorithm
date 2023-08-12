N = int(input())
lst = list(range(1, N+1))
i = 0
# i가 가리키는 위치 전까지는 버린 카드라고 생각
while True:
    if N == 1:  # 카드가 하나일 경우 종료
        break
    i += 1  # 카드 버림
    lst.append(lst[i])  # i에 있는 카드 아래로 옮김
    i += 1  # 카드 옮김

    if i == len(lst) - 1:   # i가 마지막 카드를 가리킬 때 종료
        break

print(lst[i])