nums = [int(input()) for _ in range(5)]
# 버블 정렬
for i in range(4, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

sum_v = 0
for i in nums:
    sum_v += i

print(sum_v//5)
print(nums[2])