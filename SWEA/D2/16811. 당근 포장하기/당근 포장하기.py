T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 당근의 개수
    C = sorted(list(map(int, input().split())))     # 당근의 크기
    lengths = []

    # 당근 2개를 선택하여 세 구간으로 나누고, 조건에 만족하는지 확인
    chk = False
    for i in range(1, N//2+1):
        if C[i-1] != C[i]:  # 이전 당근이랑 중복이 아닐 경우
            for j in range(i+1, N):
                if C[j-1] != C[j]:
                    S, M, L = C[:i], C[i:j], C[j:]   # 소/중/대
                    if len(S) <= N//2 and len(M) <= N//2 and len(L) <= N//2:    # 최대 길이를 넘지 않을 경우
                        lengths.append(max(len(S),len(M),len(L)) - min(len(S),len(M),len(L)))
                        chk = True  # 포장했음을 표시

    if chk: print(f'#{tc} {min(lengths)}')
    else: print(f'#{tc} -1')