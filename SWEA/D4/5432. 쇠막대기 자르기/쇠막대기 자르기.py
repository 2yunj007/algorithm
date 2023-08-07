T = int(input())
for tc in range(1, T+1):
    b = input()

    # 레이저 '()'를 '*'로 바꿈
    bar = b.replace('()','*')

    # 총 길이
    len_bar = 0
    for _ in bar:
        len_bar += 1

    op = 0    # 열린 괄호 수
    cnt = 0     # 조각 수

    for i in range(len_bar):
        if bar[i] == '(':   # 괄호가 열리면 조각 수 추가
            op += 1
            cnt += 1
        elif bar[i] == ')':
            op -= 1
        else:   # 레이저를 만나면, 현재 열린 괄호만큼 조각이 추가됨
            cnt += op

    print(f'#{tc} {cnt}')
