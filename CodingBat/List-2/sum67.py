def sum67(nums):
  rango = False
  suma = 0
  for i in nums:
    if i == 6:
      rango = True
    if not rango:
      suma += i
    if rango and i == 7:
      rango = False
  return suma


print(sum67([1, 2, 2]))# → 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))# → 5
print(sum67([1, 1, 6, 7, 2]))# → 4