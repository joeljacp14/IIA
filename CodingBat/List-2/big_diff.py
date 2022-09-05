def big_diff(nums):
  minor = nums[0]
  major = nums[0]
  for i in nums:
    minor = min(minor, i)
    major = max(major, i)
  return major - minor


print(big_diff([10, 3, 5, 6]))# → 7
print(big_diff([7, 2, 10, 9]))# → 8
print(big_diff([2, 10, 7, 2]))# → 8