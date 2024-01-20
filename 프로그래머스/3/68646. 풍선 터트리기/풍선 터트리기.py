def solution(a):
    answer = 0
    N = len(a)

    left, right = 1e9, 1e9
    check = [0] * N

    for i in range(N):
        if a[i] < left:
            left = a[i]
            check[i] = 1

        if a[N-i-1] < right:
            right = a[N-i-1]
            check[N-i-1] = 1

    answer += sum(check)

    return answer