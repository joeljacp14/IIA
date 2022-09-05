def max_end3(nums):
  mayor = 0
  if nums[0] > nums[2]:
    mayor = nums[0]
  else:
    mayor = nums[2]
  for i in range(len(nums)):
    nums[i] = mayor
  return nums


print(max_end3([1, 2, 3]))# → [3, 3, 3]
print(max_end3([11, 5, 9]))#→ [11, 11, 11]
print(max_end3([2, 11, 3]))# → [3, 3, 3]