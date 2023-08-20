N = int(input())
nums = [int(input()) for _ in range(N)]
# 버블 정렬
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
# 출력
for i in nums:
    print(i)