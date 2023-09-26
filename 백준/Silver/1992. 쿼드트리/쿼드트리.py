def f(r, c, n):
    # 첫 번째 칸의 데이터를 저장
    data = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            # 첫 번째 칸과 다른 데이터가 나오면 네 구간으로 분할
            if arr[i][j] != data:
                # 분할하면 괄호 열고 끝나면 닫음
                print('(', end='')
                f(r, c, n//2)             # 왼쪽 위
                f(r, c+n//2, n//2)        # 오른쪽 위
                f(r+n//2, c, n//2)        # 왼쪽 아래
                f(r+n//2, c+n//2, n//2)   # 오른쪽 아래
                print(')', end='')
                return
    print(data, end='')


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
f(0, 0, N)