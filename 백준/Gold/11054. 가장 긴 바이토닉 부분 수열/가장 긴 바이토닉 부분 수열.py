import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp_i = [1]*N    # 증가 부분
dp_d = [1]*N    # 감소 부분

# 자기자신 왼쪽에 있는 수가 증가하는 수인지 확인
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_i[i] = max(dp_i[i], dp_i[j]+1)

# 자기자신 오른쪽에 있는 수가 감소하는 수인지 확인
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dp_d[i] = max(dp_d[i], dp_d[j]+1)

rst = [0]*N
for i in range(N):
    rst[i] = dp_i[i] + dp_d[i] - 1

print(max(rst))