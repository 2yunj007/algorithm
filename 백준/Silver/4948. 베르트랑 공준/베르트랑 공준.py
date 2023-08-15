import sys
input = sys.stdin.readline

# 소수인지 확인
def decimal(x):
    if x == 1:
        return False
    for k in range(2, int(x**0.5)+1):
        if x % k == 0:
            return False
    return True


# 가능한 모든 수가 소수인지 확인 후 소수 명단에 넣기
# 테스트케이스마다 소수인지 확인하면 시간 초과 나기 때문에
# 미리 소수 리스트를 만들어 둠
decimal_nums = []
for i in range(2, 246912):
    if decimal(i):
        decimal_nums.append(i)

# 반복문을 통해 케이스를 확인
while True:
    n = int(input())
    cnt = 0
    # 입력이 0이면 종료
    if n == 0:
        break
    # 소수인 수를 반복하여 구간에 있는지 확인
    for j in decimal_nums:
        # 구간에 있다면 카운트
        if n < j <= 2*n:
            cnt += 1
    print(cnt)