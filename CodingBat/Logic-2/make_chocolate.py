def make_chocolate(small, big, goal):
  residuo = 0
  if goal >= 5 * big:
    residuo = goal - 5 * big
  else:
    residuo = goal % 5
  if residuo <= small:
    return residuo
  return -1


print(make_chocolate(4, 1, 9))# → 4
print(make_chocolate(4, 1, 10))# → -1
print(make_chocolate(4, 1, 7))# → 2