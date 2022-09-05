def same_first_last(nums):
  length = len(nums)
  if length  >= 1:
    if nums[0] == nums[length - 1]:
      return True
  return False


print(same_first_last([1, 2, 3]))# → False
print(same_first_last([1, 2, 3, 1]))# → True
print(same_first_last([1, 2, 1]))# → True