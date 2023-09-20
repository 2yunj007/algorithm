def f(i, N, total):
    global cnt
    # 정답을 N개 골랐고 정답 수가 5 이상이라면
    if i == N and total >= 5:
        cnt += 1
        return
    # 정답을 N개 골랐지만 정답 수가 5 이상이 아니라면
    elif i == N:
        return
    # 4문제 남았는데 정답 수가 0이라면
    elif i == N - 4 and total == 0:
        return

    for j in range(1, 6):
        marking[i] = j
        # 3개 연속으로 같은 숫자일 경우
        if i >= 2 and marking[i] == marking[i - 1] == marking[i - 2]:
            continue
        # 정답일 경우
        if arr[i] == marking[i]:
            f(i + 1, N, total + 1)
        else:
            f(i + 1, N, total)


import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
N = len(arr)
marking = [0] * N
cnt = 0
f(0, N, 0)
print(cnt)