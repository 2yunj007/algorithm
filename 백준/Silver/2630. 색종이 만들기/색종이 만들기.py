def f(r, c, n):
    # 첫 번째 칸의 색을 저장
    color = arr[r][c]
    flag = True
    for i in range(r, r+n):
        for j in range(c, c+n):
            # 첫 번째 칸과 다른 색이 나오면 네 구간으로 분할
            if arr[i][j] != color:
                f(r, c, n//2)
                f(r, c+n//2, n//2)
                f(r+n//2, c+n//2, n//2)
                f(r+n//2, c, n//2)
                flag = False
                break
        if not flag:
            break
    if flag:
        cnt[color] += 1
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0]    # white, black
f(0, 0, N)
print(cnt[0])
print(cnt[1])