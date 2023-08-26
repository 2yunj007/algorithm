T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) >= len(B):
        long, short = A, B
    else:
        long, short = B, A

    max_v = 0
    for i in range(len(long)-len(short)+1):
        sum_v = 0
        for j in range(len(short)):
            sum_v += long[i+j]*short[j]
        if sum_v > max_v:
            max_v = sum_v
    print(f'#{tc} {max_v}')