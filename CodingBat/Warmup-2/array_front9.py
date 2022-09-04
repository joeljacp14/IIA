def array_front9(nums):
  if len(nums) <= 4:
    for i in range(len(nums)):
      if nums[i] == 9:
        return True
  else:
    for i in range(4):
      if nums[i] == 9:
        return True
  return False


print(array_front9([1, 2, 9, 3, 4]))# → True
print(array_front9([1, 2, 3, 4, 9]))# → False
print(array_front9([1, 2, 3, 4, 5]))# → False