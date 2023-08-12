N, K = map(int, input().split())
lst = list(range(1, N+1))
rst = []    # 삭제할 원소 받을 리스트
i = 0   # 인덱스

while lst:
    i += K - 1
    if i >= len(lst):   # 리스트를 넘어가면 넘어가는 만큼 i 재할당
        i %= len(lst)
    rst.append(lst.pop(i))  # i 위치에 있는 원소 삭제 후 rst에 담음

print('<', end='')
for j in range(N):
    if j == N - 1:
        print(f'{rst[j]}>')
    else:
        print(f'{rst[j]}', end=', ')