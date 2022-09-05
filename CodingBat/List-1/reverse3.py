def reverse3(nums):
  aux = nums[0]
  nums[0] = nums[2]
  nums[2] = aux
  return nums


print(reverse3([1, 2, 3]))# → [3, 2, 1]
print(reverse3([5, 11, 9]))# → [9, 11, 5]
print(reverse3([7, 0, 0]))# → [0, 0, 7]