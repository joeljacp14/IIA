def sum13(nums):
  if len(nums) == 0:
    return 0
  suma = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      suma += nums[i]
      i += 1
    else:
      i += 2
  return suma


print(sum13([1, 2, 2, 1]))# → 6
print(sum13([1, 1]))# → 2
print(sum13([1, 2, 2, 1, 13]))# → 6