N = int(input())
state = list(map(int, input()))
answer = list(map(int, input()))


def switch(lst):
    cnt = 0
    for i in range(1, N):
        # i - 1번째 상태가 정답과 다르면 스위칭
        if lst[i - 1] != answer[i - 1]:
            cnt += 1
            for j in range(i - 1, i + 2):
                if j < N:
                    lst[j] ^= 1

    if lst == answer:
        return cnt
    return int(1e10)


# 0번째 스위치를 누르지 않았을 경우
cnt = switch(state.copy())
# 0번째 스위치를 눌렀을 경우
state[0] ^= 1
state[1] ^= 1
cnt = min(cnt, switch(state.copy()) + 1)

if cnt == int(1e10):
    print(-1)
else:
    print(cnt)