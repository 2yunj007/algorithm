N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 저장
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i - 1] + arr[i]

# 누적합을 M 으로 나눈 나머지를 Key, 그 개수를 Value 로 갖는 dictionary 생성
arr_dict = {}
for i in range(N):
    arr_dict.setdefault(dp[i] % M, 0)
    arr_dict[dp[i] % M] += 1

# Key 값이 0 이 있다면 result 더하기
if 0 in arr_dict.keys():
    result = arr_dict[0]
else:
    result = 0
    
# (arr[j-1] - arr[i]) % m = 0이 되는 구간을 구해야 함
# 분배법칙을 사용하면  arr[j-1] % m = arr[i] % m 
# 즉, 누적합을 M 으로 나눈 나머지가 같은 값끼리는 2개씩 골라서 구간을 만들 수 있으므로
# nC2 계산 : (n * (n - 1)) // 2
for v in arr_dict.values():
    result += (v * (v - 1)) // 2
print(result)