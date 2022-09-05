def sum2(nums):
  length = len(nums)
  if length == 1:
    return nums[0]
  if length == 0:
    return 0
  return nums[0] + nums[1]


print(sum2([1, 2, 3]))#→ 3
print(sum2([1, 1]))# → 2
print(sum2([1, 1, 1, 1]))# → 2
