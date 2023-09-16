# 최댓값과 최솟값을 곱함

N = int(input())
nums = list(map(int, input().split()))
print(max(nums) * min(nums))