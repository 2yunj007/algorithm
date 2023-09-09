'''
LCS(최장 공통 부분 수열): 두 수열이 주어졌을 때, 모든 부분 수열이 되는 수열 중 가장 긴 부분
1. ACAYKP를 비교 대상으로 잡고 CAPCAK 문자열 하나씩 추가하면서 공통 수열 길이 값을 DP에 표시
2. 문자열이 같으면 왼쪽 대각선 위의 값에 +1
3. 문자열이 같지 않으면 왼쪽 값과 위쪽 값 중 큰 값을 넣음
4. DP의 마지막 값인 DP[-1][-1]의 값이 LCS의 길이
'''
S1 = list(input())
S2 = list(input())
len1 = len(S1)
len2 = len(S2)
dp = [[0]*(len2+1) for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len1][len2])
