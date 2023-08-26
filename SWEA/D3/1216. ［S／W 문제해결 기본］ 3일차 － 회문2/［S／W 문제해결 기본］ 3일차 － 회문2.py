for _ in range(10):
    tc = int(input())
    arr = [input() for i in range(100)]
    max_l = 0

    # 가로 회문 검사
    for i in range(100):
        for j in range(100):
            s = ''
            for k in range(100-j):
                s += arr[i][j+k]
                if s == s[::-1] and len(s) > max_l:
                    max_l = len(s)

    # 세로 회문 검사
    for i in range(100):
        for j in range(100):
            s = ''
            for k in range(100-j):
                s += arr[j+k][i]
                if s == s[::-1] and len(s) > max_l:
                    max_l = len(s)

    print(f'#{tc} {max_l}')