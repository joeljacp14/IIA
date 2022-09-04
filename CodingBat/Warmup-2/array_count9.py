def array_count9(nums):
  cont = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      cont += 1
  return cont


print(array_count9([1, 2, 9]))# → 1
print(array_count9([1, 9, 9]))# → 2
print(array_count9([1, 9, 9, 3, 9]))# → 3