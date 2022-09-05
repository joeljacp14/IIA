def rotate_left3(nums):
  aux = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = aux
  return nums


print(rotate_left3([1, 2, 3]))# → [2, 3, 1]
print(rotate_left3([5, 11, 9]))# → [11, 9, 5]
print(rotate_left3([7, 0, 0]))# → [0, 0, 7]