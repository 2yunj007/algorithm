# 일꾼 한 명의 최대 수익
def sell_honey(lst):
    global M, C
    max_total = 0   # 최대 총 수익

    # 비트 연산자를 사용하여 부분집합의 합을 구함
    for i in range(1 << M):
        chk = 0   # 최대 채취 가능 양을 초과하는지 확인할 변수
        total = 0   # 총 수익
        for j in range(M):
            if i & (1 << j):
                chk += lst[j]   # 채취한 벌꿀 양 증가
                total += lst[j] ** 2    # 벌꿀 판매 수익 계산
        # 최대 채취 가능 양을 초과하지 않았을 경우
        if chk <= C:
            # 최대 총 수익과 비교
            if total > max_total:
                max_total = total

    return max_total


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # 벌통의 크기, 벌통의 개수, 채취 최대 양
    arr = [list(map(int, input().split())) for _ in range(N)]
    h1 = []    # 두 일꾼이 선택한 벌통
    h2 = []
    rst = 0    # 두 일꾼이 꿀을 채취하여 얻을 수 있는 최대 수익

    for r1 in range(N):
        for c1 in range(N - M + 1):
            # 첫 번째 일꾼 선택
            h1 = arr[r1][c1:c1 + M]
            # 첫 번째 일꾼이 선택한 벌통과 겹치지 않는 벌통 중에서 두 번째 일꾼 선택
            for r2 in range(N):
                for c2 in range(N - M + 1):
                    h2 = arr[r2][c2:c2 + M]
                    # 두 번째 일꾼이 처음으로 선백한 벌꿀이
                    # 첫 번째 일꾼이 선택한 벌꿀과 겹칠 수 있는 범위 내에 있으면 제외
                    if r1 == r2 and c1 - M < c2 < c1 + M:
                        continue
                    # 두 일꾼이 겹치지 않도록 벌꿀을 선택했을 경우
                    v = sell_honey(h1) + sell_honey(h2)
                    if v > rst:
                        rst = v

    print(f'#{tc} {rst}')
