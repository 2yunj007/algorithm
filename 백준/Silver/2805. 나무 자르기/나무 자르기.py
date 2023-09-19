import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

hieght = range(max(tree) + 1)     # 0부터 나무의 최대 높이까지가 절단기 높이의 범위

start, end = 0, max(tree)

while start <= end:
    middle = (start + end) // 2   # 나무를 자를 위치
    total_get = 0                 # 총 얻는 나무의 길이

    # 얻는 나무 길이 계산
    for i in range(N):
        if tree[i] > middle:
            total_get += tree[i] - middle

    # M 이상 얻었다면 오른쪽 범위 재탐색
    # 높이의 최댓값을 구해야 하기 때문에 더 높은 높이로 설정
    if total_get >= M:
        start = middle + 1

    # M 미만으로 얻었다면 왼쪽 범위 재탐색
    # 더 낮은 높이로 설정
    elif total_get < M:
        end = middle - 1

print(hieght[end])