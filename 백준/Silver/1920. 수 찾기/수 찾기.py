def BinarySearch(start, end, target):
    # 찾지 못했을 경우
    if start > end:
        return 0

    middle = (start + end) // 2

    # middle이 target인 경우
    if A[middle] == target:
        return 1

    # middle이 target보다 작은 경우 오른쪽 탐색
    if A[middle] < target:
        return BinarySearch(middle + 1, end, target)

    # middle이 target보다 큰 경우 왼쪽 탐색
    if A[middle] > target:
        return BinarySearch(start, middle - 1, target)


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for target in B:
    print(BinarySearch(0, N - 1, target))
