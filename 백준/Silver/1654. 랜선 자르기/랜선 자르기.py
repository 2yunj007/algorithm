import sys
input = sys.stdin.readline

K, N = map(int, input().split())
K_lst = []

for _ in range(K):
    K_lst.append(int(input()))

max_len = sum(K_lst) // N   # 임의의 최대 랜선 길이
lan = range(max_len+1)  # 이진 탐색을 위한 리스트

start = 1    # 랜선의 최솟값은 1
end = max_len

# 이진 탐색
while start <= end:
    middle = (start + end) // 2
    tmp = 0
    # middle에 있는 랜선 길이로 나눈 몫들을 tmp에 누적합
    for k in K_lst:
        tmp += k // lan[middle]
    # 만약 tmp가 N보다 크거나 같다면 오른쪽 부분에 대해 재탐색
    # 없다면 현재 값이 최대 길이일 거임
    if tmp >= N:
        start = middle + 1
    # tmp가 N보다 작다면 길이가 너무 길다는 거니까 왼쪽 부분에 대해 재탐색
    else:
        end = middle - 1

# start == end가 됐을 때 하나 남은 값이 랜선의 최대 길이
print((start+end)//2)
