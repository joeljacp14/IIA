def make_ends(nums):
  if len(nums) >= 1:
    return [nums[0], nums[-1]]
  return [0, 0]


print(make_ends([1, 2, 3]))#→ [1, 3]
print(make_ends([1, 2, 3, 4]))# → [1, 4]
print(make_ends([7, 4, 6, 2]))#→ [7, 2]