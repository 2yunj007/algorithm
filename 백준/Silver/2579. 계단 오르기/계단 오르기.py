# 한 칸 혹은 두 칸씩 이동 가능
# 세 칸 연속으로는 못 밟음
# 마지막 칸 밟아야 함
N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]     # 점수, 연속으로 밟은 칸

# 각 칸까지 가는 최댓값 저장하기
# 3번째 칸까지는 직접 최댓값 할당
dp[0][0], dp[0][1] = stairs[0], 1

if N > 1:
    dp[1][0], dp[1][1] = stairs[0] + stairs[1], 2

if N > 2:
    third_stair1 = stairs[2] + stairs[1]
    third_stair2 = stairs[2] + stairs[0]
    if third_stair1 > third_stair2:
        dp[2][0], dp[2][1] = third_stair1, 2
    else:
        dp[2][0], dp[2][1] = third_stair2, 1

    for i in range(3, N):
        stair1 = dp[i - 1][0] + stairs[i]
        stair2 = dp[i - 2][0] + stairs[i]
        stair3 = dp[i - 3][0] + stairs[i - 1] + stairs[i]

        if stair1 >= stair3 and stair1 > stair2 and dp[i - 1][1] == 1:
            dp[i][0], dp[i][1] = stair1, 2
        elif stair3 > stair2:
            dp[i][0], dp[i][1] = stair3, 2
        else:
            dp[i][0], dp[i][1] = stair2, 1
        
print(dp[N - 1][0])