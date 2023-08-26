def danjo(n): # 1234
    global max_v
    if n < max_v:   # 현재 최댓값보다 작으면 x
        return

    num = n
    while num != 0:
        num1 = num % 10   # 뒷 자리 수 값
        num //= 10
        num2 = num % 10   # 앞 자리 수 값
        if num1 < num2:   # 뒷 자리 수 값이 앞 자리 수 값보다 작으면 x
            return
    max_v = n

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0

    # 숫자 두 개를 선택
    for i in range(N-1):
        for j in range(i+1, N):
            danjo(arr[i] * arr[j])

    if max_v == 0:  # 단조 증가 수가 없으면 -1 출력
        max_v = -1
    print(f'#{tc} {max_v}')