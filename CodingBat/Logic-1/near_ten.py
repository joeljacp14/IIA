def near_ten(num):
  mod = num % 10
  if mod == 2 or mod == 9 or mod == 8 or mod == 1 or mod == 0:
    return True
  return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))