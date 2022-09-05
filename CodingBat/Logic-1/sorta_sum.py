def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum


print(sorta_sum(3, 4))# → 7
print(sorta_sum(9, 4)) #→ 20
print(sorta_sum(10, 11))# → 21