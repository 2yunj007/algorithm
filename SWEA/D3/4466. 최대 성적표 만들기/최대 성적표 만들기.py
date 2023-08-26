T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 과목 수, 성적표에 넣을 과목
    score = list(map(int, input().split()))
    max_s = 0

    for i in range(K):
        max_s += sorted(score)[N-1-i]

    print(f'#{tc} {max_s}')